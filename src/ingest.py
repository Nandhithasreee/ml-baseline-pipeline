import pandas as pd
import os
from sklearn.datasets import fetch_california_housing

def load_and_save_data(output_path="data/raw/raw_data.csv"):
    """
    Downloads raw dataset and persists it to data/raw.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print("Fetching dataset...")
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    df.to_csv(output_path, index=False)
    print(f"Raw data successfully saved to {output_path} (Shape: {df.shape})")
    return df

if __name__ == "__main__":
    load_and_save_data()