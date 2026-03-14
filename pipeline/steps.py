from pipeline.base import PipelineStep
import csv
import json

class ExtractStep(PipelineStep):
    def __init__(self, name, source):
        super().__init__(name)
        self.source = source
        
    def execute(self, data=None):
        if isinstance(self.source, list):
            return self.source
        else:
            with open(self.source, 'r') as f :
                reader = csv.DictReader(f)
                return list(reader)
            
class TransformStep(PipelineStep):
    def __init__(self, name, transform_fn):
        super().__init__(name)
        self.transform_fn = transform_fn
    
    def execute(self, data):
        return self.transform_fn(data)
    
class LoadStep(PipelineStep):
    def __init__(self, name, destination):
        super().__init__(name)
        self.destination = destination
    
    def execute(self,data):
        if callable(self.destination):
            return self.destination(data)
        else:
            with open(self.destination, 'w') as j:
                json.dump(data, j, indent = 2)
        
        
        
        