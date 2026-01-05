from pydantic import BaseModel
from typing import List, Optional


class PredictionResult(BaseModel):
    label: str
    confidence: float


class SinglePredictionResponse(BaseModel):
    filename: str
    prediction: str
    confidence: float
    all_predictions: List[PredictionResult]


class BatchPredictionItem(BaseModel):
    filename: str
    prediction: str
    confidence: float
    all_predictions: List[PredictionResult]


class BatchPredictionResponse(BaseModel):
    results: List[BatchPredictionItem]
    total: int


class ExportRequest(BaseModel):
    results: List[dict]


class HealthResponse(BaseModel):
    status: str
    version: str
