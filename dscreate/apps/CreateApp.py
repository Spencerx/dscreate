from .BaseApp import DsCreate, dscreate_flags 
from traitlets import Bool, default
from .. import preprocessors


class CreateApp(DsCreate):

    name = u'dscreate-create'
    description = u'Split a jupyter notebook into student facing and teacher facing files.'
    flags = create_flags

    

    @default("classes")
    def _classes_default(self) -> List[MetaHasTraits]:
        classes = super(CreateApp, self)._classes_default()

        for pr_name in preprocessors.__all__:
            pr = getattr(preprocessors, pr_name)
            if pr.class_traits(config=True):
                classes.append(pg)

        return classes

    
# Git commit
# init notebook - Run cells
# Collect resources
# 