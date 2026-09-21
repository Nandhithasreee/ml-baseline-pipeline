# Machine Learning Baseline Pipeline

A modular pipeline for data ingestion, preprocessing, baseline model training, and evaluation reporting.

## Directory Structure
- `src/ingest.py`: Fetches and persists raw datasets.
- `src/preprocess.py`: Implements feature scaling and train-test splitting.
- `src/train.py`: Fits a baseline Ridge Regression model.
- `src/evaluate.py`: Generates metric benchmark reports.
- `main.py`: Orchestrates the complete end-to-end execution.

## Quickstart

1. Install dependencies:
   ```bash
   pip install -r requirements.txt