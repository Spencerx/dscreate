from .BaseApp import DsCreate, dscreate_flags 
from traitlets import Bool, default
from .. import preprocessors


create_flags = {'dir': ({'CreateApp': {'dir': True}}, 
"Write solution files to `.solution_files` instead of a solution branch")}
create_flags.update(dscreate_flags)

class CreateApp(DsCreate):

    name = u'dscreate-create'
    description = u'Split a jupyter notebook into student facing and teacher facing files.'
    flags = create_flags


    dir = Bool()
    @default('dir')
    def dir_default(self) -> bool:
        return False

    @default("classes")
    def _classes_default(self) -> List[MetaHasTraits]:
        classes = super(CreateApp, self)._classes_default()

        for pr_name in preprocessors.__all__:
            pr = getattr(preprocessors, pr_name)
            if pr.class_traits(config=True):
                classes.append(pg)

        return classes

    
