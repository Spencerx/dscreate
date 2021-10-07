from .BaseConverter import BaseConverter
from ..preprocessors import *
import io
import os
from nbformat import read
from nbformat.v4 import new_notebook
from traitlets import default, List, Unicode


class MergeConverter(BaseConverter):

    name = 'MergeConverter'
    printout = 'Merging notebooks...'
    description = '''
    MergeConverter reads in lesson and solution notebooks and merges them into an edit file.
    '''

    preprocessors = List([SortCells]).tag(config=True)
    output = Unicode(u'curriculum').tag(config=True)

    def read_notebook(self, filepath):
        with io.open(filepath, mode="r", encoding="utf-8") as file:
            nb = read(file, as_version=4)
        return nb

    def paths(self):
        lesson_path = self.config.BaseConverter.output + '.ipynb'
        solution_path = os.path.join(self.config.BaseConverter.solution_dir, 
                                   lesson_path)
        return lesson_path, solution_path

    def start(self) -> None:
        nb = new_notebook()

        # Read in notebooks
        lesson, solution = self.paths()
        lesson_nb = self.read_notebook(lesson)
        solution_nb = self.read_notebook(solution)

        # Concatenate cells
        nb.cells.extend(lesson_nb.cells)
        nb.cells.extend(solution_nb.cells)

        # Setup BaseConverter's write_notebook
        self.config.source_notebook = nb

        super(MergeConverter, self).start()

    


