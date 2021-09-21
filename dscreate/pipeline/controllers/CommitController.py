from .BaseController import BaseController
from .. import DsPipeline
from git import GitCommandError
from traitlets import Bool, Unicode, Int

class CommitController(BaseController):

    commit_msg = Unicode(config=True)
    count = Int(config=True)
    enabled = Bool(config=True)

    def add_and_commit(self, commit_msg=None):
        self.git.add(".")
        try:
            self.git.commit("-m", commit_msg if commit_msg else self.commit_msg)
        except GitCommandError:
            print("nothing to commit, working tree clean")

    def start(self) -> None:
        self.add_and_commit()
        self.config.CommitController.count = self.count + 1
