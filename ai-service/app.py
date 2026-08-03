from fastapi import FastAPI
from pydantic import BaseModel

from predictor import predict_defect

app = FastAPI(
    title="Lincode AI Prediction Service",
    version="1.0.0"
)


class PredictionRequest(BaseModel):
    filename: str


@app.get("/")
def root():
    return {
        "service": "Lincode AI Prediction Service",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "AI Prediction Service"
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    """
    Dummy AI prediction.
    """

    result = predict_defect(request.filename)

    return {
        "filename": request.filename,
        "prediction": result["prediction"],
        "confidence": result["confidence"]
    }
