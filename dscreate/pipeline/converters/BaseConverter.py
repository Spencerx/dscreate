import os
import typing
from traitlets import List, Bool, default, Instance, Type, Unicode
from traitlets.config import LoggingConfigurable, Config
from nbconvert.exporters import Exporter, NotebookExporter
from nbconvert.writers import FilesWriter

converter_flags = {'inline': ({'BaseConverter': {'inline': True}}, 
"Write solution files to `.solution_files` instead of a solution branch")}

class BaseConverter(LoggingConfigurable):

    name = u'dscreate-base-converter'
    flags = converter_flags
    writer = Instance(FilesWriter)
    exporter = Instance(Exporter)
    exporter_class = Type(NotebookExporter, klass=Exporter).tag(config=True)
    preprocessors = List([])
    solution = Bool(False)
    
    solution_dir = Unicode(config=True)
    @default('solution_dir')
    def solution_dir_default(self) -> None:
        cwd = os.getcwd()
        return u'{}'.format(os.path.join(cwd, '.solution_files'))


    inline = Bool(config=True)
    @default('inline')
    def inline_default(self) -> bool:
        return False

    output_name = Unicode(config=True)
    @default('output_name')
    def output_name_default(self) -> str:
        return u'index'

    notebook_path = Unicode(config=True)
    @default('notebook_path')
    def notebook_path_default(self) -> str:
        return os.path.join(os.getcwd() + 'index.ipynb')

    def __init__(self, **kwargs: typing.Any) -> None:
        """
        Set up configuration file.
        """
        super(BaseConverter, self).__init__(**kwargs)
        c = Config()
        c.Exporter.default_preprocessors = []
        self.update_config(c)

    def start(self) -> None:
        """
        Activate the converter
        """
        self.writer = FilesWriter(parent=self, config=self.config)
        self.exporter = self.exporter_class(parent=self, config=self.config)
        self._init_preprocessors()
        self.convert_notebook()

    def _init_preprocessors(self) -> None:
        """
        Here we add the preprocessors to the exporter pipeline
        with the `register_preprocessor` method.
        """
        for pp in self.preprocessors:
            self.exporter.register_preprocessor(pp)

    def convert_notebook(self) -> None:
        """
        1. Create a resources object that tells the exporter how to format link urls for images.
        2. Pass the notebook through the preprocessor and convert to the desired format via the exporter.
        3. Write the notebook to file.
        """
        resources = self.init_notebook_resources()
        output, resources = self.exporter.from_filename(self.notebook_path, resources=resources)
        self.write_notebook(output, resources)

    def init_notebook_resources(self) -> dict:
        """
        The resources argument, when passed into an exporter,
        tell the exporter what directory to include in the url 
        for external images via `output_files_dir`. 

        The `output_name` value is required by nbconvert and is typically 
        the name of the original notebook.
        """
        resources = {}
        resources['unique_key'] = self.output_name
        resources['output_files_dir'] = f'{self.output_name}_files'
        return resources

    def write_notebook(self, output, resources) -> None:
        """
        Sets the output directory for the file write
        and writes the file to disk. 
        """
        if self.inline and self.solution:
            if not os.path.exists(self.solution_dir):
                os.mkdir(self.solution_dir)
            self.writer.build_directory = self.solution_dir 

        self.writer.write(output, resources, notebook_name=resources['unique_key'])

    

        
        

        