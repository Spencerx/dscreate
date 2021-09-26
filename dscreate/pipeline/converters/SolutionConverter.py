from .BaseConverter import BaseConverter
from ..preprocessors import *

from traitlets import default


class SolutionConverter(BaseConverter):

    name = 'SolutionConverter'
    printout = 'Updating solution branch...'
    description = '''
    SolutionConverter generates the teacher facing  notebook.
    '''

    @default('solution')
    def solution_default(self) -> bool:
        return True

    @default('preprocessors')
    def preprocessors_default(self) -> list:
        if not self.config.inline.enabled:
            return [RemoveLessonCells, ExecuteCells]
        elif self.config.inline.enabled:
            return [ClearOutput, AddCellIndex, RemoveLessonCells, ExecuteCells]

    def start(self) -> None:

        if self.config.inline.enabled:
            self.config.inline.solution = True

        super(SolutionConverter, self).start()


