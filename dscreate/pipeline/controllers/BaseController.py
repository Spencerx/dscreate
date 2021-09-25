from traitlets import Unicode, Bool, default
from traitlets.config import Configurable, Config
import typing
from git import Repo

class BaseController(Configurable, Repo):

    name = 'Writing notebook...'
    
    enabled = Bool(config=True)
    @default('enabled')
    def enabled_default(self) -> bool:
        return True

    def __init__(self, **kwargs) -> None:
        """
        1. Set up configuration file.
        2. Inherit git repo attributes
        """
        Configurable.__init__(self, **kwargs)
        Repo.__init__(self, '.')



    
