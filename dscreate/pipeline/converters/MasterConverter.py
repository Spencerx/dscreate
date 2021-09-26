from .BaseConverter import BaseConverter
from ..preprocessors import ClearOutput, RemoveSolutions

from traitlets import default

class MasterConverter(BaseConverter):

    name = 'MasterConverter'
    printout = 'Updating master branch...'
    description = '''
    The master converter is used to generate the student facing notebook.

    The preprocessors default to the nbconvert ClearOutput and dscreate RemoveSolutions preprocessors.
    '''

    @default('preprocessors')
    def preprocessors_default(self) -> list:
        return [ClearOutput, RemoveSolutions]

    def start(self) -> None:

        if self.config.inline.enabled:
            self.config.inline.solution = False

        super(MasterConverter, self).start()
