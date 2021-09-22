
from git import GitCommandError
from traitlets import Bool, Unicode, default

from .. import DsPipeline
from . import CommitController, BaseController


class PushController(BaseController):

    name = 'push-controller'

    enabled = Bool(config=True)
    remote = Unicode(config=True)
    @default('remote')
    def branch_default(self) -> str:
        return u'origin'

    def get_branch(self):
        if not isinstance(self.config.CommitController.count, int):
            return self.config.DsPipeline.branches[0]

        return self.config.DsPipeline.branches[self.config.CommitController.count - 1]

    def start(self) -> None:
        branch = self.get_branch()
        self.git.push(self.remote, branch)