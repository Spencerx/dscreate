from traitlets import Set
from .BasePreprocessor import DsCreatePreprocessor


class RemoveLessonCells(DsCreatePreprocessor):

    solution_tags = Set({'#__SOLUTION__', '#==SOLUTION==', '__SOLUTION__', '==SOLUTION=='},
            help=("Tags indicating which cells are to be removed"
            )).tag(config=True)


    def is_solution(self, cell):
        """
        Checks that a cell has a solution tag. 
        """

        lines = set(cell.source.split("\n"))

        return self.solution_tags.intersection(lines)

    def preprocess(self, nb, resources):

        # Skip preprocessing if the list of patterns is empty
        if not self.solution_tags:
            return nb, resources

        # Filter out cells that meet the conditions
        cells = []
        for cell in nb.cells:
            if self.is_solution(cell) or cell.cell_type == 'markdown':
                cells.append(self.preprocess_cell(cell))
        nb.cells = cells

        return nb, resources

    def preprocess_cell(self, cell):
        """
        Removes the solution tag from the solution cells.
        """

        lines = cell.source.split('\n')
        no_tags = [line for line in lines if line not in self.solution_tags]
        cell.source = '\n'.join(no_tags)
        return cell
