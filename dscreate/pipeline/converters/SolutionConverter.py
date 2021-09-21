from .BaseConverter import BaseConverter
from ..preprocessors import *

from traitlets import default


class SolutionConverter(BaseConverter):

    @default('solution')
    def solution_default(self) -> bool:
        return True

    @default('preprocessors')
    def preprocessors_default(self) -> list:
        if self.inline:
            return [RemoveLessonCells, ExecuteCells]
        elif self.inline:
            return [ClearOutput, AddCellIndex, RemoveLessonCells, ExecuteCells]

