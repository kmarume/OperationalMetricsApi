from fastapi import APIRouter
from app.schemas.metric import MetricCreate, MetricResponse
from datetime import datetime, timezone

router = APIRouter(prefix="/metrics", tags=["Metrics"])

@router.post("/", response_model=MetricResponse)
def create_metric(metric: MetricCreate):
    return {
        "id": 1,
        "name": metric.name,
        "value": metric.value,
        "timestamp": metric.timestamp or datetime.now(timezone.utc)
    }

@router.get("/{metric_id}", response_model=MetricResponse)
def get_metric(metric_id: int):
    return {
        "id": metric_id,
        "name": "cpu_usage",
        "value": 72.5,
        "timestamp": datetime.now(timezone.utc)
    }