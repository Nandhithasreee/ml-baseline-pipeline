# Model Integration & Load Testing Pipeline

## Overview
This repository contains the serving layer and integration testing pipeline for our Machine Learning model.

- **Backend Framework:** FastAPI
- **Frontend Dashboard:** Streamlit
- **Integration Testing:** Pytest
- **Load Testing Tool:** Locust

---

## Load Testing Metrics (50 Concurrent Users)

| Metric | Observed Value |
| :--- | :--- |
| **Concurrent Users** | 50 |
| **Throughput (RPS)** | ~180 req/sec |
| **Average Latency** | 48 ms |
| **Median Latency (p50)** | 45 ms |
| **95th Percentile Latency (p95)** | 72 ms |
| **Failure Rate** | 0.0% |

---

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt