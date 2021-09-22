from traitlets import Set
from .BasePreprocessor import DsCreatePreprocessor


class RemoveSolutions(DsCreatePreprocessor):

    code_tags = Set({'#__SOLUTION__', '#==SOLUTION=='},
            help=("Tags indicating which cells are to be removed"
            )).tag(config=True)

    markdown_tags = Set({'==SOLUTION==','__SOLUTION__'}).tag(config=True)


    def is_code_solution(self, cell):
        """
        Checks that a cell has a tag that is to be removed
        Returns: Boolean.
        True means cell should *not* be removed.
        """
        lines = set(cell.source.split("\n"))

        return self.code_tags.intersection(lines)

    def is_markdown_solution(self, cell):
        lines = set(cell.source.split("\n"))
        return  self.markdown_tags.intersection(lines)

    def preprocess(self, nb, resources):

        # Skip preprocessing if the list of patterns is empty
        if not self.code_tags.union(self.markdown_tags):
            return nb, resources

        cells = []
        # Filter out cells that meet the conditions
        for cell in nb.cells:
            if self.is_code_solution(cell):
                continue
            
            if self.is_markdown_solution(cell):
                cell.source = 'YOUR ANSWER HERE'

            cells.append(cell)

        nb.cells = cells
            
        return nb, resources

