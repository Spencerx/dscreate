import os
from traitlets import List, Config, Bool, default, Instance, Type, Unicode
from nbconvert.exporters import Exporter, NotebookExporter
from nbconvert.writers import FilesWriter

converter_flags = {'inline': ({'BaseConverter': {'inline': True}}, 
"Write solution files to `.solution_files` instead of a solution branch")}

class BaseConverter:

    name = u'dscreate-base-converter'
    flags = converter_flags
    writer = Instance(FilesWriter)
    exporter = Instance(Exporter)
    exporter_class = Type(NotebookExporter, klass=Exporter).tag(config=True)
    preprocessors = List([])

    
    solution_dir = Unicode(config=True)
    @default('solution_dir')
    def solution_dir_default(self) -> None:
        cwd = os.getcwd()
        return os.path.join(cwd, '.solution_files')

    solution = Bool()
    @default('solution')
    def solution_default(self) -> bool:
        return False

    inline = Bool(config=True)
    @default('inline')
    def inline_default(self) -> bool:
        return False

    output_name = Unicode(config=True)
    @default('output_name')
    def output_name_default(self) -> str:
        return 'index'

    def start(self) -> None:
        self.writer = FilesWriter(parent=self, config=self.config)
        self.exporter = self.exporter_class(parent=self, config=self.config)
        self._init_preprocessors()
        self.convert_notebook()

    def _init_preprocessors(self) -> None:
        self.exporter._preprocessors = []
        self.exporter.default_preprocessors = []

        for pp in self.preprocessors:
            self.exporter.register_preprocessor(pp)

    def convert_notebook(self, notebook_path) -> None:
        resources = self.init_notebook_resources()
        output, resources = self.exporter.from_filename(notebook_path, resources=resources)
        self.write_notebook(output, resources)

    def init_notebook_resources(self) -> dict:
        resources = {}
        resources['unique_key'] = self.output_name
        resources['output_files_dir'] = f'{self.output_name}_files'
        return resources

    def write_notebook(self, output, resources) -> None:
        if self.inline and self.solution:
            if not os.path.exists(self.solution_dir):
                os.mkdir(self.solution_dir)

            self.writer.build_directory = self.solution_dir 
            self.writer.write(output, resources, notebook_name=resources['unique_key'])

        
        

        