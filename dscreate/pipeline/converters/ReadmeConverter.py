from . import BaseConverter
from nbconvert.exporters import MarkdownExporter
from traitlets import default, Unicode
import os

class ReadmeConverter(BaseConverter):

    name = 'Generating README...'

    exporter_class = MarkdownExporter
    notebook_path = Unicode(config=True)
    output = 'README'

    @default('notebook_path')
    def notebook_path_default(self) -> str:
        if self.config.inline.enabled and self.config.inline.solution:
            return os.path.join(self.solution_dir,  'index.ipynb')
        
        return 'index.ipynb'

    @default('preprocessors')
    def preprocessors_default(self) -> list:
        return []

    def convert_notebook(self) -> None:
        """
        1. Create a resources object that tells the exporter how to format link urls for images.
        2. Pass the notebook through the preprocessor and convert to the desired format via the exporter.
        3. Write the notebook to file.
        """
        resources = self.init_notebook_resources()
        output, resources = self.exporter.from_filename(self.notebook_path, resources=resources)
        self.write_notebook(output, resources)
