from traitlets import Set
from .BasePreprocessor import DsCreatePreprocessor


class RemoveCodeSolution(DsCreatePreprocessor):

    code_tags = Set({'#__SOLUTION__', '#==SOLUTION=='},
            help=("Tags indicating which cells are to be removed"
            )).tag(config=True)


    def check_cell_conditions(self, cell, resources, index):
        """
        Checks that a cell has a tag that is to be removed
        Returns: Boolean.
        True means cell should *not* be removed.
        """
        lines = set(cell.source.split("\n"))

        return not self.code_tags.intersection(lines)

    def preprocess(self, nb, resources):

        # Skip preprocessing if the list of patterns is empty
        if not self.code_tags:
            return nb, resources

        # Filter out cells that meet the conditions
        nb.cells = [self.preprocess_cell(cell, resources, index)[0]
                    for index, cell in enumerate(nb.cells)
                    if self.check_cell_conditions(cell, resources, index)
                    and cell.cell_type == 'code']

        return nb, resources

    def preprocess_cell(self, cell, resources, cell_index):
        """
        No transformation is applied.
        """
        
        return cell, resources
