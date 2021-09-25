from .BaseController import BaseController
from .. import DsPipeline
from git import GitCommandError
from traitlets import Bool
from . import CommitController

class CheckoutEditBranch(BaseController):

    name = 'Checking out the edit branch...'

    def start(self) -> None:
        edit_branch = self.config.traversed_branches[0]
        self.git.checkout(edit_branch)
