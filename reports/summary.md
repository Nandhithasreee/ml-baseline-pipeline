# Core Model + Experimentation Summary

## Overview
We trained a primary **Random Forest Classifier** baseline model and evaluated performance across **3 different hyperparameter configurations** using MLflow experiment tracking.

## Experimentation Results

| Run Name | n_estimators | max_depth | min_samples_split | Accuracy | Precision | Recall | F1 Score |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Config_1_Baseline | 50 | 3 | 2 | 0.9474 | 0.9459 | 0.9722 | 0.9589 |
| Config_2_Medium | 100 | 5 | 5 | 0.9561 | 0.9589 | 0.9722 | 0.9655 |
| **Config_3_Deeper (Best)** | **200** | **10** | **2** | **0.9649** | **0.9595** | **0.9861** | **0.9726** |

## Best Configuration Evidence
* **Best Model:** `Config_3_Deeper`
* **Optimal Hyperparameters:** `n_estimators=200`, `max_depth=10`, `min_samples_split=2`
* **Peak Metrics:** Accuracy = **96.49%**, F1-Score = **0.9726**
* **Artifacts Generated:** 
  * Serialized Best Model: `models/best_model.pkl`
  * Confusion Matrix Plot: `reports/cm_Config_3_Deeper.png`
  * MLflow Experiment Logs: Saved in `./mlruns`