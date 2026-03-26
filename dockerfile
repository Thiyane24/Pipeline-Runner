FROM python:3.12-alpine

WORKDIR /app

COPY pipeline/ ./pipeline/
COPY data/     ./data/
COPY test_pipeline.py .

RUN mkdir -p output

CMD ["python", "test_pipeline.py"]