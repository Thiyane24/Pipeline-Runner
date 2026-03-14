from abc import ABC, abstractmethod

class PipelineStep(ABC):
    '''Abstract class representing a step in the pipeline.'''
    def __init__(self,name, status ="pending"):
        self.name = name
        self.status = status
        
    def __repr__(self):
        return f"PipelineStep (name = '{self.name}', status = '{self.status}')"
    
    @abstractmethod
    def execute(self,data):
        raise NotImplementedError("Subclasses must implement execute")

        
         
         