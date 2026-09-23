from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.model import model

app = FastAPI(title="ML Model Serving API", version="1.0.0")

class PredictRequest(BaseModel):
    features: List[float]

class PredictResponse(BaseModel):
    predictions: List[float]
    status: str

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "ML Model API"}

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    if not request.features:
        raise HTTPException(status_code=400, detail="Feature list cannot be empty.")
    
    try:
        output = model.predict(request.features)
        return output
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))