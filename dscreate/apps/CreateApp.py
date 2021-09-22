from .BaseApp import DsCreate, dscreate_flags, dscreate_aliases
from traitlets import Bool, default, List, Unicode
from traitlets.config import Config
from typing import List as TypingList
from traitlets.traitlets import MetaHasTraits
from ..pipeline import *
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


    
    def start(self) -> None:
        super().start()

        c = Config()
        c.edit_branch = self.edit_branch
        c.DsPipeline.steps = self.pipeline_steps
        c.DsPipeline.branches = self.branches
        c.merge(self.config)
        pipeline = DsPipeline(config=c)
        pipeline.start()