from .BaseApp import DsCreate, dscreate_flags, dscreate_aliases
from traitlets import Bool, default, List, Unicode
from traitlets.config import Config
from typing import List as TypingList
from traitlets.traitlets import MetaHasTraits
from ..pipeline import *
import os
from .. import pipeline


edit_aliases = {
    'output': 'MergeConverter.out',
    'solution_dir':'BaseConverter.solution_dir',
    'concat': 'SortCells.enabled',
    }

class EditApp(DsCreate):

    name = u'edit'
    description = u'''
    Generates an edit file for an in directory notebook split.
    
    **Behavior:**

    1. 

    '''
    
    aliases = edit_aliases
    
    pipeline_steps = List([MergeConverter]).tag(config=True)
          
    def start(self) -> None:
        super(EditApp, self).start()
        self.config.DsPipeline.steps = self.pipeline_steps
        self.config.DsPipeline.branches = []
        pipeline = DsPipeline(config=self.config)
        pipeline.start()