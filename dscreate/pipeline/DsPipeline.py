from traitlets.config import Configurable
from traitlets import List

class DsPipeline(Configurable):

    def __init__(self, **kwargs) -> None:
        """
        Set up configuration file.
        """
        super(DsPipeline, self).__init__(**kwargs)
    
    
    steps = List(config=True)
    branches = List(config=True)
    
    def start(self) -> None:
        for step in self.steps:
            pipeline_step = step(config=self.config)
            print('\n', pipeline_step.name)
            pipeline_step.start()
            self.config.merge(pipeline_step.config)