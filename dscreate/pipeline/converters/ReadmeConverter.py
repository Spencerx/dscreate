from . import BaseConverter
from nbconvert.exporters import MarkdownExporter

class ReadmeConverter(BaseConverter):

    exporter_class = Markdownexporter

    @default('notebook_path')
    def notebook_path_default(self) -> str:
        if self.inline and self.config.inline_tacker == 1:
            return os.path.join(self.solution_dir,  'index.ipynb')
