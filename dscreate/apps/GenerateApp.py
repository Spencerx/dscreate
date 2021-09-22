from .BaseApp import DsCreate, dscreate_aliases
from traitlets import Bool, default, List, Unicode
from traitlets.config import Config
from typing import List as TypingList
from traitlets.traitlets import MetaHasTraits
from ..pipeline import *
from .. import pipeline

generate_flags = {
    'api': (
        {'use_api' : {'enabled' : True}},
        "If True the nbgrader API will be used to split the notebook, which requires that the assignment is placed in the source folder of an nbgrader course."
    ),
}

generate_aliases = {}
generate_aliases.update(dscreate_aliases)


class GenerateApp(DsCreate):

    name = u'dscreate-generate'
    description = u'Split an nbgrader assignment into student facing and teacher facing files.'
    flags = generate_flags
    aliases = generate_aliases


    edit_branch = Unicode(config=True)
    @default('edit_branch')
    def edit_branch_default(self) -> str:
        return 'master'

    pipeline_steps = List(config=True)
    @default('pipeline_steps')
    def pipeline_steps_default(self) -> TypingList:

        return [
            CollectCurriculum,
            BaseConverter,
            ReleaseConverter,
            Commit,
            Push,

            Checkout,
            BaseConverter,
            SourceConverter,
            Commit,
            Push,
            CheckoutEditBranch,
            ]


    branches = List(config=True)
    @default('branches')
    def branches_default(self):
        return ['master', 'solution']


    @default("classes")
    def _classes_default(self) -> TypingList[MetaHasTraits]:
        classes = super(GenerateApp, self).all_configurable_classes()

        return classes

    
    def start(self) -> None:
        super().start()

        c = Config()
        c.edit_branch = self.edit_branch
        c.DsPipeline.steps = self.pipeline_steps
        c.DsPipeline.branches = self.branches
        c.merge(self.config)
        pipeline = DsPipeline(config=c)
        pipeline.start()