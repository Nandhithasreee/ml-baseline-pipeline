from locust import HttpUser, task, between

class ModelLoadTestUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(3)
    def predict_endpoint(self):
        payload = {"features": [1.2, 3.4, 5.6, 7.8]}
        self.client.post("/predict", json=payload)

    @task(1)
    def health_check(self):
        self.client.get("/")