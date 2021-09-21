from nbconvert.preprocessors import ClearOutputPreprocessor
from .BasePreprocessor import DsCreatePreprocessor

class ClearOutput(DsCreatePreprocessor, ClearOutputPreprocessor):
    pass