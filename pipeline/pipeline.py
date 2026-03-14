from pipeline.logger import Logger
import time
class Pipeline:
    def __init__ (self, name):
        '''Class representing a data pipeline. It manages the execution of multiple PipelineStep instances in sequence.'''
        self.name = name
        self.steps = []
    
    def add_step(self, step):
        '''Adds a PipelineStep to the pipeline. Returns self to allow method chaining.'''
        self.steps.append(step)
        return self
        
    def run(self, data = None):
        '''Executes all steps in the pipeline in sequence. It logs the start and end of each step, along with the execution time.'''
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
        '''Prints a summary of the pipeline execution, including the name of the pipeline and the status of each step.'''
        print(f"Pipeline: {self.name}")
        for step in self.steps:  
         print(f"{step.name} -> {step.status}")
        