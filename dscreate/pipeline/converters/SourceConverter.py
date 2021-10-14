from . import BaseConverter
from traitlets import default, Unicode, Type
from nbconvert.exporters import MarkdownExporter, Exporter


class SourceConverter(BaseConverter):

    name = 'SourceConverter'
    printout = 'Updating solution branch...'
    description = '''
    SourceConverter generates a teacher facing readme for an nbgrader assignment.
    '''
    exporter_class = Type(MarkdownExporter, klass=Exporter).tag(config=True)

    notebook_path = Unicode('index.ipynb').tag(config=True)
    output = Unicode(u'README').tag(config=True)



        

        