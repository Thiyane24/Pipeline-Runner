class Pipeline:
    def __init__ (self, name):
        self.name = name
        self.steps = []
    
    def add_step(self, step):
        self.steps.append(step)
        return self
        
    def run(self, data = None):
        result = data 
        for step in self.steps:
            result = step.execute(result)
            step.status = "done"
            
        return result        
    
    def summary(self):
       print(f"Pipeline: {self.name}")
       for step in self.steps:  
        print(f"{step.name} -> {step.status}")
        