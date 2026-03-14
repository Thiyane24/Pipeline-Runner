# 🚀 Pipeline Runner

> A lightweight, composable ETL pipeline framework built in pure Python, modelling the same architecture used by Apache Airflow, Prefect, and Luigi.

---

## 📌 Overview

**Pipeline Runner** is the second project in my OOP Python Data Engineering series. It implements a modular ETL (Extract, Transform, Load) pipeline system using abstract base classes, composition, and the Strategy design pattern.

The goal was to build a system where individual pipeline steps are independent, reusable, and composable the same mental model behind production-grade orchestration tools.

---

## 🏗️ Architecture

```
pipeline/
├── __init__.py
├── base.py         # Abstract PipelineStep base class
├── steps.py        # ExtractStep, TransformStep, LoadStep
├── pipeline.py     # Pipeline orchestrator
└── logger.py       # Execution logger with timing
```

---

## ⚙️ Classes

### `PipelineStep` (Abstract Base Class)
The abstract parent for all pipeline steps. Enforces that every step implements `execute()`.

```python
from abc import ABC, abstractmethod

class PipelineStep(ABC):
    def __init__(self, name, status="pending"):
        self.name = name
        self.status = status

    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("Subclasses must implement execute")
```

### `ExtractStep`
Reads data from a source — either a CSV filepath or a list of dicts passed directly.

```python
step = ExtractStep("extract", source="data/sales.csv")
data = step.execute()
```

### `TransformStep`
Applies a transformation function to the data. The function is injected at construction time (Strategy Pattern).

```python
def remove_nulls(data):
    return [row for row in data if any(row.values())]

step = TransformStep("clean", transform_fn=remove_nulls)
data = step.execute(data)
```

### `LoadStep`
Writes the final data to a destination — either a JSON filepath or a callable.

```python
step = LoadStep("load", destination="output/result.json")
step.execute(data)
```

### `Pipeline`
Orchestrates a sequence of steps. Passes the output of each step as the input to the next.

```python
pipeline = Pipeline("sales_etl")
pipeline.add_step(ExtractStep("extract", "data/sales.csv"))
        .add_step(TransformStep("clean", remove_nulls))
        .add_step(LoadStep("load", "output/result.json"))

pipeline.run()
```

### `Logger`
Wraps step execution with timing and status logging.

```
[RUNNING] extract...
[DONE]    extract    (0.043s)
[RUNNING] clean...
[DONE]    clean      (0.012s)
[RUNNING] load...
[DONE]    load       (0.008s)
```

---

## 🧠 OOP Concepts Practised

| Concept | Where Used |
|---|---|
| Abstract Classes | `PipelineStep` uses `ABC` and `@abstractmethod` |
| Composition | `Pipeline` holds a list of `PipelineStep` objects |
| Strategy Pattern | `TransformStep` stores a function as an attribute |
| Method Chaining | `add_step()` returns `self` |
| Status Tracking | Each step tracks its own `status` |
| Inheritance | `ExtractStep`, `TransformStep`, `LoadStep` inherit from `PipelineStep` |

---

## 🔗 DE Context

This project mirrors the core architecture of **Apache Airflow**:

| This Project | Airflow Equivalent |
|---|---|
| `Pipeline` | DAG |
| `PipelineStep` | BaseOperator |
| `ExtractStep` | PythonOperator (extract) |
| `TransformStep` | PythonOperator (transform) |
| `LoadStep` | PythonOperator (load) |
| `Logger` | Airflow task logs |

Understanding how to model a pipeline as a sequence of composable steps is one of the most fundamental skills in Data Engineering.

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/Thiyane24/pipeline-runner
cd pipeline-runner

# Run the test pipeline
python test_pipeline.py
```

No external dependencies standard library only.

---

## 📋 Requirements

- Python 3.8+
- No third-party libraries required

---

## 📁 Part of

This project is part of my **OOP Python Data Engineering Series** — 7 projects building from beginner to intermediate DE skills.

| # | Project | Status |
|---|---|---|
| 01 | CSV Data Parser & Cleaner | ✅ Complete |
| 02 | Pipeline Runner | 🔄 In Progress |
| 03 | Database Connection Pool | ⏳ Upcoming |
| 04 | Schema Registry | ⏳ Upcoming |
| 05 | Data Quality Framework | ⏳ Upcoming |
| 06 | Mini Message Queue | ⏳ Upcoming |
| 07 | Batch Job Scheduler | ⏳ Upcoming |

---

## 👤 Author

**Thiyane Xavier**
IT Diploma Student @ MAHSA University, Malaysia
Aspiring Data Engineer | Python | SQL

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Thiyane%20Xavier-blue)](https://www.linkedin.com/in/thiyane-xavier-9aa09a345/)
[![GitHub](https://img.shields.io/badge/GitHub-Thiyane24-black)](https://github.com/Thiyane24)