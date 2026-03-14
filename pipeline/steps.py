from pipeline.base import PipelineStep
import csv
import json

class ExtractStep(PipelineStep):
    def __init__(self, name, source):
        '''Initializes the ExtractStep with a name and a data source. The source can be a file path or a list of dictionaries.'''
        super().__init__(name)
        self.source = source
        
    def execute(self, data=None):
        '''Executes the extraction step. If the source is a list, it returns the list. If the source is a file path, it reads the file and returns its contents as a list of dictionaries.'''
        if isinstance(self.source, list):
            return self.source
        else:
            with open(self.source, 'r', encoding='utf-8') as f :
                reader = csv.DictReader(f)
                return list(reader)
            
class TransformStep(PipelineStep):
    '''Initializes the TransformStep with a name and a transformation function. The transformation function is a callable that takes data as input and returns transformed data.'''
    def __init__(self, name, transform_fn):
        super().__init__(name)
        self.transform_fn = transform_fn
    
    def execute(self, data):
        return self.transform_fn(data)
    
class LoadStep(PipelineStep):
    '''Initializes the LoadStep with a name and a destination. The destination can be a file path or a callable function that takes data as input.'''
    def __init__(self, name, destination):
        super().__init__(name)
        self.destination = destination
    
    def execute(self,data):
        if callable(self.destination):
            return self.destination(data)
        else:
            with open(self.destination, 'w') as j:
                json.dump(data, j, indent = 2)
        
        
        
        