from pipeline.steps import ExtractStep
from pipeline.steps import TransformStep
from pipeline.steps import LoadStep
from pipeline.logger import Logger
from pipeline.pipeline import Pipeline

def remove_empty_rows(data):
    return [row for row in data if all(row.values())]

extract_step1 = ExtractStep("extract", source = "data/Messy_Employee_dataset.csv")
transform_step1 = TransformStep("remove_empty_rows", transform_fn = remove_empty_rows)
load_step1 = LoadStep("load", "output/result.json")
pipeline1 = Pipeline("Pipeline 1")
pipeline1.add_step(extract_step1).add_step(transform_step1).add_step(load_step1)
pipeline1.run() 
pipeline1.summary()

print("\n" + "="*50 + "\n")

extract_step = ExtractStep("extract", source = "data/Uncleaned_DS_jobs.csv")

transform_step = TransformStep("transform", transform_fn = remove_empty_rows)

load_step = LoadStep("load", "output/result1.json")

pipeline2 = Pipeline("Pipeline 2")
pipeline2.add_step(extract_step).add_step(transform_step).add_step(load_step)
pipeline2.run()
pipeline2.summary()

print("\n" + "="*50 + "\n")

extract3 = ExtractStep('extract', source = "data/datos_sucios.csv")
transform3 = TransformStep('transform', transform_fn = remove_empty_rows)
load3 = LoadStep('load', "output/result3.json")
pipeline3 = Pipeline("Pipeline 3")
pipeline3.add_step(extract3).add_step(transform3).add_step(load3)
pipeline3.run()
pipeline3.summary()
