from .BasePreprocessor import DsCreatePreprocessor

class SortCells(DsCreatePreprocessor):

    description = '''
    Sorts the cells of a notebook according to the metadata.index variable
    and adds a solution tag back to solution cells.
    '''
    
    def preprocess(self, nb, resources):

        # Sort cells
        cells = list(sorted(nb.cells, key=lambda x: x['metadata']['index']))

        # Remove duplicates
        nb.cells = []
        indices = []
        for idx, cell in enumerate(cells):
            if cell['metadata']['index'] not in indices:
                nb.cells.append(self.preprocess_cell(cell, resources, idx)[0])
                indices.append(cell['metadata']['index'])

        return nb, resources

    def preprocess_cell(self, cell, resources, cell_index):

        # Add solution tag to solution cells
        if cell['metadata']['solution']:
            if cell.cell_type == 'code':
                cell.source = '#==SOLUTION==\n' + cell.source
            else:
                cell.source = '==SOLUTION==\n' + cell.source

        return cell, resources
