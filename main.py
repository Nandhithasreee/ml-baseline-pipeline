from src.ingest import load_and_save_data
from src.preprocess import preprocess_data
from src.train import train_baseline_model
from src.evaluate import evaluate_baseline

def run_pipeline():
    print("--- [Step 1/4] Ingesting Data ---")
    load_and_save_data()
    
    print("\n--- [Step 2/4] Preprocessing Data ---")
    preprocess_data()
    
    print("\n--- [Step 3/4] Training Baseline Model ---")
    train_baseline_model()
    
    print("\n--- [Step 4/4] Evaluating Model Benchmark ---")
    evaluate_baseline()
    
    print("\n pipeline execution completed successfully!")

if __name__ == "__main__":
    run_pipeline()