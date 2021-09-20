from traitlets import Set
from .BasePreprocessor import DsCreatePreprocessor


class RemoveLessonCells(DsCreatePreprocessor):

    solution_tags = Set({'#__SOLUTION__', '#==SOLUTION==', '__SOLUTION__', '==SOLUTION=='},
            help=("Tags indicating which cells are to be removed"
            )).tag(config=True)


    def check_cell_conditions(self, cell, resources, index):
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
        nb.cells = [self.preprocess_cell(cell, resources, index)[0]
                    for index, cell in enumerate(nb.cells)
                    if self.check_cell_conditions(cell, resources, index)
                    or cell.cell_type == 'markdown']

        return nb, resources

    def preprocess_cell(self, cell, resources, cell_index):
        """
        Removes the solution tag from the solution cells.
        """

        lines = cell.source.split('\n')
        no_tags = [line for line in lines if line not in self.solution_tags]
        cell.source = '\n'.join(no_tags)
        return cell, resources
