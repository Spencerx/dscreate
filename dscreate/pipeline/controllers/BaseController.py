from traitlets import Unicode
from traitlets.config import Configurable, Config
import typing
from git import Repo

class BaseController(Configurable, Repo):


    def __init__(self, **kwargs) -> None:
        """
        1. Set up configuration file.
        2. Inherit git repo attributes
        """
        Configurable.__init__(self, **kwargs)
        Repo.__init__(self, '.')



    
