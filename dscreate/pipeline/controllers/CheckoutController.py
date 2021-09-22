from .BaseController import BaseController
from .. import DsPipeline
from git import GitCommandError
from traitlets import Bool
from . import CommitController

class CheckoutController(BaseController):

    name = 'checkout-controller'

    def get_branch(self):
        if not isinstance(self.config.CommitController.count, int):
            self.config.CommitController.count = 0
        return self.config.DsPipeline.branches[self.config.CommitController.count]

    def merge_edit_branch(self):
        current_branch = self.active_branch
        edit_branch = self.branches[self.config.edit_branch]
        base = self.merge_base(current_branch, edit_branch)
        self.index.merge_tree(edit_branch, base=base)
        self.index.commit(f'Merge {edit_branch} into {current_branch.name}.', 
        parent_commits=(current_branch.commit, edit_branch.commit))

    def start(self) -> None:
        active_branch = self.active_branch.name
        if not isinstance(self.config.traversed_branches, list):
            self.config.traversed_branches = []
        self.config.traversed_branches.append(active_branch)
        
        branch = self.get_branch()
        self.git.checkout(branch)
        self.merge_edit_branch()
