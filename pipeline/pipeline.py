from pipeline.logger import Logger
import time
class Pipeline:
    def __init__ (self, name):
        self.name = name
        self.steps = []
    
    def add_step(self, step):
        self.steps.append(step)
        return self
        
    def run(self, data = None):
        logger = Logger()
        result = data 
        for step in self.steps:
            start = time.perf_counter()
            logger.log_start(step)
            result = step.execute(result)
            end = time.perf_counter()
            duration = end - start 
            logger.log_end(step, duration)
            step.status = "done"
        
        return result        
    
    def summary(self):
       print(f"Pipeline: {self.name}")
       for step in self.steps:  
        print(f"{step.name} -> {step.status}")
        