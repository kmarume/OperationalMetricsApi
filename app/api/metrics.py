from fastapi import APIRouter, HTTPException
from app.schemas.metric import MetricCreate, MetricResponse
from datetime import datetime, timezone
from app.services import metrics_service

router = APIRouter(prefix="/metrics", tags=["Metrics"])

@router.post("/", response_model=MetricResponse)
def create_metric(metric: MetricCreate):
    return metrics_service.create_metric(metric)

@router.get("/{metric_id}", response_model=MetricResponse)
def get_metric(metric_id: int):
    metric = metrics_service.get_metric(metric_id)
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")
    return metric