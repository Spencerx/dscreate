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
        active_branch = self.active_branch.name
        if not isintance(self.config.traversed_branches, list):
            self.config.traversed_branches = []
        self.config.traversed_branches.append(active_branch)
        
        branch = self.get_branch()
        self.git.checkout(branch)