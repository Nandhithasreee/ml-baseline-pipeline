import pandas as pd
import joblib
import os
from sklearn.linear_model import Ridge

def train_baseline_model(
    processed_dir="data/processed",
    model_dir="models",
    random_state=42
):
    """
    Loads preprocessed training data and trains a baseline Ridge Regression model.
    """
    os.makedirs(model_dir, exist_ok=True)
    
    X_train = pd.read_csv(os.path.join(processed_dir, "X_train.csv"))
    y_train = pd.read_csv(os.path.join(processed_dir, "y_train.csv")).values.ravel()
    
    # Train baseline Ridge Regression
    model = Ridge(alpha=1.0, random_state=random_state)
    model.fit(X_train, y_train)
    
    # Save trained baseline model artifact
    model_path = os.path.join(model_dir, "baseline_model.pkl")
    joblib.dump(model, model_path)
    print(f"Baseline model trained and saved to {model_path}")

if __name__ == "__main__":
    train_baseline_model()