import time
class Logger:
    def log_start(self,step):
        print(f"[RUNNING] {step.name}...")
    
    def log_end(self,step, duration):
        print(f"[DONE]  {step.name}   ({duration:.3f}s)")
    
    def log_error(self, step, error):
        print(f"[FAILED]  {step.name} - {error}")