import os
import typing
from traitlets import List, Bool, default, Instance, Type, Unicode
from traitlets.config import Configurable, Config
from nbconvert.exporters import Exporter, NotebookExporter
from nbconvert.writers import FilesWriter


class BaseConverter(Configurable):

    name = u'dscreate-base-converter'
    writer = Instance(FilesWriter)
    exporter = Instance(Exporter)
    exporter_class = Type(NotebookExporter, klass=Exporter).tag(config=True)
    preprocessors = List([], config=True)
    solution = Bool(False)

    enabled = Bool(config=True)
    @default('enabled')
    def enabled_default(self) -> bool:
        return True
    
    solution_dir = Unicode(config=True)
    @default('solution_dir')
    def solution_dir_default(self) -> None:
        cwd = os.getcwd()
        return u'{}'.format(os.path.join(cwd, '.solution_files'))

    output = Unicode(config=True)
    @default('output')
    def output_name_default(self) -> str:
        return u'index'

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
        self.exporter = self.exporter_class(config=self.config)
        self._init_preprocessors()
        self.convert_notebook()
        if self.config.inline.enabled:
            self.config.inline.tracker += 1

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
        output, resources = self.exporter.from_notebook_node(self.config.source_notebook, resources=resources)
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
        resources['unique_key'] = self.output
        resources['output_files_dir'] = f'{self.output}_files'
        return resources

    def write_notebook(self, output, resources) -> None:
        """
        Sets the output directory for the file write
        and writes the file to disk. 
        """
        if self.config.inline.enabled and self.solution:
            if not os.path.exists(self.solution_dir):
                os.mkdir(self.solution_dir)
            self.writer.build_directory = self.solution_dir 

        self.writer.write(output, resources, notebook_name=self.output)



    

        
        

        