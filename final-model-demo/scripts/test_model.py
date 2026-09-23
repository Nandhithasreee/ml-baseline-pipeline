import os
import joblib
import numpy as np

def test_model_training():
    from scripts.train import train
    train()
    assert os.path.exists("model.pkl"), "Model file was not created!"

def test_model_inference():
    model = joblib.load("model.pkl")
    sample_input = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction = model.predict(sample_input)
    assert len(prediction) == 1, "Inference output shape mismatch!"