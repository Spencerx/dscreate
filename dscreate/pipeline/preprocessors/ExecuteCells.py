from nbconvert.preprocessors import ExecutePreprocessor
from .BasePreprocessor import DsCreatePreprocessor

class ExecuteCells(DsCreatePreprocessor, ExecutePreprocessor):
    pass