import pytest 
import os
from .base import BaseTestConverter
from ...pipeline import BaseConverter
from nbformat import read

class TestBaseConverter(BaseTestConverter):

    def test_run_converter(self, dir_test, config) -> None:
        os.chdir(dir_test)
        converter = BaseConverter(config=config)
        converter.start()

        

