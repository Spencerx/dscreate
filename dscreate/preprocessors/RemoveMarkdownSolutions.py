from traitlets import Set
from .BasePreprocessor import DsCreatePreprocessor

class RemoveMarkdownSolution(DsCreatePreprocessor):

    markdown_tags = Set({'==SOLUTION==', '__SOLUTION__'},
            help=("Tags indicating which cells are written answer cells."
            )).tag(config=True)

    def check_cell_conditions(self, cell, resources, index):
        """
        Checks that a cell has a tag indicating a written solution.
        Returns true if the cell is a written solution
        """
        lines = set(cell.source.split("\n"))

        return self.markdown_tags.intersection(lines)

    def preprocess(self, nb, resources):

        # Skip preprocessing if the list of patterns is empty
        if not self.markdown_tags:
            return nb, resources

        # Preprocess cells
        nb.cells = [self.preprocess_cell(cell, resources, index)[0] 
        if self.check_cell_conditions(cell, resources, index)
        and cell.cell_type == 'markdown'
        else cell for index, cell in enumerate(nb.cells)]

        return nb, resources

    def preprocess_cell(self, cell, resources, cell_index):

        cell.source = 'YOUR ANSWER HERE'

        return cell, resources