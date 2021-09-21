from traitlets.config import LoggingConfigurable
from traitlets import List

class DsPipeline(LoggingConfigurable):
    
    
    steps = List(config=True)
    
    def start(self) -> None:
        for step in self.steps:
            pipeline_step = step(config=self.config)
            pipeline_step.start()
            self.config.merge(pipeline_step.config)