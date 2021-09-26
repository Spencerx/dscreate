from .BaseApp import DsCreate, dscreate_flags, dscreate_aliases
from traitlets import Bool, default, List, Unicode
from traitlets.config import Config
from typing import List as TypingList
from traitlets.traitlets import MetaHasTraits
from ..pipeline import *
from git import Repo
import os
from .. import pipeline

create_flags = {
    'inline': (
    {'DsCreate': {'inline': True},
     'CollectCurriculum': {'edit_file': 'curriculum.ipynb'}}, "Create inline directory split.")
}

class CreateApp(DsCreate):

    name = u'create'
    description = u'''
    Splits a notebook into student and teacher facing materials using dscreate solution tags.
    
    **Behavior:**

    CreateApp uses three major variables.

    1. ``pipeline_steps``
        * This variable is a list containing the converters and controllers that are applied to the repository.
    2. ``branches``
        * This variable is a list containing the name of git branches and is used by CheckoutControllers (included in the ``pipeline_steps`` list) to move sequentially across the branches.
        * *It is worth noting that the ``pipeline_steps`` list cannot contain more CheckoutControllers than the length of ``branches``.
    3. ``inline``
        * This variable is a bool that indicates whether or not to split the notebooks on solely on the active branch. When inline is True, the solution files are stored in a ``.solution_files`` directory.
        * inline is set to True via the ``--inline`` flag.
        * When inline is true, a ``curriculum.ipynb`` file used as the ``edit_file``.

    - If a branch inside the branches list has not been created, it is created.
    - For notebook splits that requires git branches, the application must be run from the edit_branch which defaults to ``curriculum``.
    '''
    
    flags = dscreate_flags
    aliases = dscreate_aliases
    inline = Bool(False).tag(config=True)
    edit_branch = Unicode('curriculum').tag(config=True)
    
    pipeline_steps = List(config=True)
    @default('pipeline_steps')
    def pipeline_steps_default(self) -> TypingList:
        if not self.inline:
            return [
                CollectCurriculum,
                ReadmeConverter,
                Commit,
                Push,

                Checkout,
                MasterConverter,
                ReadmeConverter,
                Commit,
                Push,

                Checkout,
                SolutionConverter,
                ReadmeConverter,
                Commit,
                Push,
                CheckoutEditBranch
                ]

        return [CollectCurriculum,
                SolutionConverter,
                ReadmeConverter,
                MasterConverter,
                ReadmeConverter,
                Commit, 
                Push]


    branches = List(['curriculum', 'master', 'solution']).tag(config=True)


    def validate_branches(self) -> None:
        if not '.git' in os.listdir():
            raise ValueError('ds create must be run from the root of a git repository.')

        branches = os.path.join('.git', 'refs', 'heads')
        if self.edit_branch not in os.listdir(branches):
            raise ValueError('A curriculum branch must exist.')

        repo = Repo('.')
        if not self.inline:
            if repo.active_branch.name.lower() != self.edit_branch:
                raise ValueError(f'ds create must be run from the {self.edit_branch} branch')

        for branch in self.branches:
            if branch not in os.listdir(branches):
                print(f'Creating {branch} branch...')
                repo.create_head(branch)
                origin = repo.remote()
                origin.push(branch)
        
    
    def start(self) -> None:
        super().start()
        self.validate_branches()

        c = Config()
        c.inline.enabled = self.inline
        self.config.merge(c)
        c.edit_branch = self.edit_branch
        c.DsPipeline.steps = self.pipeline_steps
        c.BaseController.branches = self.branches
        c.merge(self.config)
        pipeline = DsPipeline(config=c)
        pipeline.start()