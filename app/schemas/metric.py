from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MetricCreate(BaseModel):
    name: str
    value: float
    timestamp: Optional[datetime] = None

class MetricResponse(BaseModel):
    id: int
    name: str
    value: float
    timestamp: datetime