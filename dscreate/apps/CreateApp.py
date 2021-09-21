from .BaseApp import DsCreate, dscreate_flags, dscreate_aliases
from traitlets import Bool, default
from .. import pipeline



class CreateApp(DsCreate):

    name = u'dscreate-create'
    description = u'Split a jupyter notebook into student facing and teacher facing files.'
    flags = dscreate_flags
    aliases = dscreate_aliases

    

    @default("classes")
    def _classes_default(self) -> List[MetaHasTraits]:
        classes = super(CreateApp, self)._classes_default()

        for pr_name in pipeline.__all__:
            pr = getattr(pipeline, pr_name)
            if pr.class_traits(config=True):
                classes.append(pg)

        return classes
    
    pipeline_steps = List([ReadmeConverter,
                           Commit,
                           Push,
                           Checkout,
                           LessonConverter,
                           ReadmeConverter,
                           Commit,
                           Push,
                           Checkout,
                           SolutionConverter,
                           ReadmeConverter,
                           Commit,
                           Push], config=True)


    branches = List(config=True)
    @default('branches')
    def branches_default(self):
        return ['curriculum', 'master', 'solution']

    
    def start(self) -> None:
        super().start()

        c = Config()
        c.Pipeline.steps = self.pipeline_steps
        c.Pipeline.branches = self.branches
        c.merge(self.config)
        pipeline = Pipeline(config=c)
        pipeline.start()