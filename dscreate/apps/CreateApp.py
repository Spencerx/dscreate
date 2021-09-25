from .BaseApp import DsCreate, dscreate_flags, dscreate_aliases
from traitlets import Bool, default, List, Unicode
from traitlets.config import Config
from typing import List as TypingList
from traitlets.traitlets import MetaHasTraits
from ..pipeline import *
from git import Repo
import os
from .. import pipeline



class CreateApp(DsCreate):

    name = u'dscreate-create'
    description = u'Split a jupyter notebook into student facing and teacher facing files.'
    flags = dscreate_flags
    aliases = dscreate_aliases


    edit_branch = Unicode(config=True)
    @default('edit_branch')
    def edit_branch_default(self) -> str:
        return 'curriculum'


    @default("classes")
    def _classes_default(self) -> TypingList[MetaHasTraits]:
        classes = super(CreateApp, self).all_configurable_classes()

        return classes
    
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


    branches = List(config=True)
    @default('branches')
    def branches_default(self):
        return ['curriculum', 'master', 'solution']


    def validate_branches(self) -> None:
        if not '.git' in os.listdir():
            raise ValueError('ds create must be run from the root of a git repository.')

        branches = os.path.join('.git', 'refs', 'heads')
        if self.edit_branch not in os.listdir(branches):
            raise ValueError('A curriculum branch must exist.')

        repo = Repo('.')

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
        c.edit_branch = self.edit_branch
        c.DsPipeline.steps = self.pipeline_steps
        c.DsPipeline.branches = self.branches
        c.merge(self.config)
        pipeline = DsPipeline(config=c)
        pipeline.start()