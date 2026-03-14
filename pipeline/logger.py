import time
class Logger:
    '''Class responsible for logging the execution of pipeline steps. It provides methods to log the start and end of each step, as well as any errors that occur during execution.'''
    def log_start(self,step):
        '''Logs the start of a pipeline step. It prints the name of the step being executed.
        '''
        print(f"[RUNNING] {step.name}...")
    
    def log_end(self,step, duration):
        '''Logs the end of a pipeline step. It prints the name of the step that has completed and the duration of its execution in seconds.'''
        print(f"[DONE]  {step.name}   ({duration:.3f}s)")
    
    def log_error(self, step, error):
        '''Logs any errors that occur during the execution of a pipeline step. It prints the name of the step and the error message.'''
        print(f"[FAILED]  {step.name} - {error}")