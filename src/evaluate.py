import pandas as pd
import numpy as np
import joblib
import json
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_baseline(
    processed_dir="data/processed",
    model_path="models/baseline_model.pkl",
    reports_dir="reports"
):
    """
    Evaluates the baseline model on the test split and outputs a metrics report.
    """
    os.makedirs(reports_dir, exist_ok=True)
    
    X_test = pd.read_csv(os.path.join(processed_dir, "X_test.csv"))
    y_test = pd.read_csv(os.path.join(processed_dir, "y_test.csv")).values.ravel()
    
    # Load trained model
    model = joblib.load(model_path)
    
    # Predict on unseen test data
    y_pred = model.predict(X_test)
    
    # Calculate evaluation benchmark metrics
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    metrics = {
        "model_type": "Ridge Regression (Baseline)",
        "metrics": {
            "MAE": round(float(mae), 4),
            "RMSE": round(float(rmse), 4),
            "R2_Score": round(float(r2), 4)
        }
    }
    
    # Save JSON report
    report_json_path = os.path.join(reports_dir, "baseline_metrics.json")
    with open(report_json_path, "w") as f:
        json.dump(metrics, f, indent=4)
        
    # Markdown Summary Report
    report_md_path = os.path.join(reports_dir, "baseline_report.md")
    with open(report_md_path, "w") as f:
        f.write("# Baseline Model Evaluation Report\n\n")
        f.write(f"- **Model Type**: {metrics['model_type']}\n")
        f.write(f"- **Mean Absolute Error (MAE)**: {metrics['metrics']['MAE']}\n")
        f.write(f"- **Root Mean Squared Error (RMSE)**: {metrics['metrics']['RMSE']}\n")
        f.write(f"- **R² Score**: {metrics['metrics']['R2_Score']}\n")
        
    print(f"Evaluation complete. Reports generated at {reports_dir}/")
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    evaluate_baseline()