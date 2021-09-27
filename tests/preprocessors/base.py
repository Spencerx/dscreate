import io
import os
from traitlets import HasTraits, List
from nbformat import read
from .. import CreateCells

class BaseTestPreprocessor(CreateCells):

    required_attributes = ['description',
                            'preprocess']

    def read_nb(self, filepath):
        with io.open(filepath, mode="r", encoding="utf-8") as file:
            nb = read(file, as_version=4)
        return nb

    def test_required_attributes(self, preprocessor) -> None:
        for attribute in BaseTestPreprocessor.required_attributes:
            assert hasattr(preprocessor,  attribute)