from . import BaseConverter
from traitlets import default, Unicode
from nbconvert.exporters import MarkdownExporter


class SourceConverter(BaseConverter):

    name = 'SourceConverter'
    printout = 'Updating solution branch...'
    description = '''
    SourceConverter generates a teacher facing readme for an nbgrader assignment.
    '''
    exporter_class = MarkdownExporter

    notebook_path = Unicode('index.ipynb').tag(config=True)
    output = 'README'



        

        