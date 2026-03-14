from pipeline.steps import ExtractStep
from pipeline.steps import TransformStep
from pipeline.steps import LoadStep
from pipeline.logger import Logger
from pipeline.pipeline import Pipeline

def remove_empty_rows(data):
    return [row for row in data if all(row.values())]

transform_step = TransformStep("clean", transform_fn=remove_empty_rows)

extract_step = ExtractStep("extract", source = "data/Messy_Employee_dataset.csv")

load_step = LoadStep("load", "output/result.json")

pipeline = Pipeline("Pipeline 1")

pipeline.add_step(extract_step).add_step(transform_step).add_step(load_step)

pipeline.run()
pipeline.summary()




