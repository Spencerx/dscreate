import pytest 
import os
from .base import BaseTestPreprocessor
from ...dscreate.pipeline.preprocessors import RemoveLessonCells
from nbformat.v4 import new_notebook

@pytest.fixture
def preprocessor():
    return RemoveLessonCells()

class TestRemoveLessonCells(BaseTestPreprocessor):

    """
    1. Test that a warning is raised if no lesson cells are found.
    2. Test differring locations for tags
    3. Test different tag formats
    4. Test changing tag configuration
    5. Test warning for when a solution tag is found but it was not found on its own line
    6. Test warning for when a solution tag found once text  has been lowered.
    7. Test cell remove for example notebook
    8. Test length of cells once lesson cells have been removed
    9. Test empty cell
    """

