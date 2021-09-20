from .BaseConverter import BaseConverter
from ..preprocessors import RemoveLessonCells, ExecuteCells


class SolutionConverter(BaseConverter):

    @default('solution')
    def solution_default(self) -> bool:
        return True

    @default('preprocessors')
    def preprocessors_default(self) -> list:
        return [RemoveLessonCells, ExecuteCells]

