from .BaseController import BaseController
from .. import DsPipeline
from git import GitCommandError
from traitlets import Bool
from . import CommitController

class CheckoutController(BaseController):

    def get_branch(self):
        if not isintance(self.config.Commit.count, int):
            raise ValueError("A CommitController must be activated before a CheckoutController.")
        return self.config.Pipeline.branches[self.config.Commit.count]

    def start(self) -> None:
        branch = self.get_branch()
        self.git.checkout(branch)