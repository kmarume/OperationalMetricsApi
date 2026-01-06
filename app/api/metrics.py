from fastapi import APIRouter

router = APIRouter(prefix="/metrics", tags=["Metrics"])

@router.post("/")
def create_metric():
    return {"message": "metric received"}

@router.get("/{metric_id}")
def get_metric(metric_id: int):
    return {
        "id": metric_id,
        "name": "cpu_usage",
        "value": 72.5
    }