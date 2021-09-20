from nbconvert.preprocessors import Preprocessor

class DsCreatePreprocessor(Preprocessor):

    enabled = Bool(True, help="Whether to use this preprocessor when running dscreate").tag(config=True)