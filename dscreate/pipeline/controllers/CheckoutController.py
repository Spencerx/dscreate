from .BaseController import BaseController
from .. import DsPipeline
from git import GitCommandError
from traitlets import Bool, Unicode, default
from . import CommitController

class CheckoutController(BaseController):

    name = Unicode(config=True)
    @default('name')
    def name_default(self) -> str:
        return 'Checking out {}...'.format(self.get_branch())

    def get_branch(self):
        if not isinstance(self.config.CommitController.count, int):
            self.config.CommitController.count = 0
        return self.config.DsPipeline.branches[self.config.CommitController.count]

    def merge_edit_branch(self):
        self.git.merge(self.config.traversed_branches[0], X='theirs')

    def start(self) -> None:
        active_branch = self.active_branch.name
        if not isinstance(self.config.traversed_branches, list):
            self.config.traversed_branches = []
        self.config.traversed_branches.append(active_branch)
        
        branch = self.get_branch()
        self.git.checkout(branch)
        self.merge_edit_branch()
