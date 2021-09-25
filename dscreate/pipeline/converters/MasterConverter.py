from .BaseConverter import BaseConverter
from ..preprocessors import ClearOutput, RemoveSolutions

from traitlets import default

class MasterConverter(BaseConverter):

    name = 'Updating master branch...'

    @default('preprocessors')
    def preprocessors_default(self) -> list:
        return [ClearOutput, RemoveSolutions]

    def start(self) -> None:
        super(MasterConverter, self).start()

        if self.config.inline.enabled:
            self.config.inline.solution = False