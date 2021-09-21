from .BaseConverter import BaseConverter
from ..preprocessors import ClearOutput, RemoveCodeSolution, RemoveMarkdownSolution

from traitlets import default

class MasterConverter(BaseConverter):

    @default('preprocessors')
    def preprocessors_default(self) -> list:
        return [ClearOutput, RemoveCodeSolution, RemoveMarkdownSolution]