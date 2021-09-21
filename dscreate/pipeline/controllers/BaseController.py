from traitlets import Unicode
from traitlets.config import LoggingConfigurable, Config
import typing
from git import Repo

class BaseController(LoggingConfigurable, Repo):


    def __init__(self, **kwargs) -> None:
        """
        1. Set up configuration file.
        2. Inherit git repo attributes
        """
        LoggingConfigurable.__init__(**kwargs)
        Repo.__init__(self, '.')



    
