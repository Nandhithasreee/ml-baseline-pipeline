import time

class MLModel:
    def __init__(self):
        # Simulate model load time
        pass

    def predict(self, input_data: list):
        # Simulate processing latency (e.g., 50ms)
        time.sleep(0.05)
        
        # Example prediction logic
        results = [float(x) * 2.5 for x in input_data]
        return {"predictions": results, "status": "success"}

model = MLModel()