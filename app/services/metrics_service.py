from typing import Dict
from datetime import datetime, timezone
from app.schemas.metric import MetricCreate, MetricResponse

_metrics_store: Dict[int, MetricResponse] = {}
_next_id = 1

def create_metric(metric: MetricCreate) -> MetricResponse:
    global _next_id

    metric_data = MetricResponse(
        id=_next_id,
        name=metric.name,
        value=metric.value,
        timestamp=metric.timestamp or datetime.now(timezone.utc)
    )

    _metrics_store[_next_id] = metric_data
    _next_id += 1

    return metric_data

def get_metric(metric_id: int) -> MetricResponse:
    return _metrics_store.get(metric_id)