from traitlets import Set, Int
from .BasePreprocessor import DsCreatePreprocessor


class AddCellIndex(DsCreatePreprocessor):

    index = Int(0)

    solution_tags = Set({'#__SOLUTION__', '#==SOLUTION==', '__SOLUTION__', '==SOLUTION=='},
            help=("Tags indicating which cells are to be removed"
            )).tag(config=True)

    def preprocess(self, nb, resources):

        # Filter out cells that meet the conditions
        nb.cells = [self.preprocess_cell(cell, resources, index)[0]
                    for index, cell in enumerate(nb.cells)]

        return nb, resources

    def preprocess_cell(self, cell, resources, cell_index):
        """
        No transformation is applied.
        """
        lines = set(cell.source.split("\n"))
        if self.solution_tags.intersection(lines):
            cell['metadata']['solution'] = True
        else:
            cell['metadata']['solution'] = False

        cell['metadata']['index'] = self.index
        self.index += 1
        return cell, resources
