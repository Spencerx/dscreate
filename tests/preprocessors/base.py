import io
import os
import pytest
from traitlets import HasTraits, List
from nbformat import read
from .. import CreateCells

class BaseTestPreprocessor(CreateCells):

    required_attributes = ['description',
                            'preprocess',
                            'enabled']

    dir_path = os.path.abspath(os.path.dirname(__file__))

    def read_nb(self, filepath):
        with io.open(filepath, mode="r", encoding="utf-8") as file:
            nb = read(file, as_version=4)
        return nb

    def test_required_attributes(self, preprocessor) -> None:
        for attribute in BaseTestPreprocessor.required_attributes:
            assert hasattr(preprocessor,  attribute)

    def notebook_path(self, directory, file_name):
        return os.path.join(BaseTestPreprocessor.dir_path, directory, file_name)

    @pytest.fixture
    def base_notebook(self):
        path = self.notebook_path('files', 'base_notebook.ipynb')
        nb = self.read_nb(path)
        return nb

    @pytest.fixture
    def preprocess_base(self, preprocessor, base_notebook):
        resources = {}
        nb, resources = preprocessor.preprocess(base_notebook, resources)
        return nb

    @pytest.fixture
    def no_lesson_cells_notebook(self):
        path = self.notebook_path('files', 'no_lesson_cells_notebook.ipynb')
        nb = self.read_nb(path)
        return nb

    @pytest.fixture
    def preprocess_no_lesson_cells(self, preprocessor, no_lesson_cells_notebook):
        resources = {}
        nb, resources = preprocessor.preprocess(no_lesson_cells_notebook, resources)
        return nb

