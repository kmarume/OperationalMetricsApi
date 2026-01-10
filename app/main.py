from fastapi import FastAPI

from app.database import Base, engine
from app.api.health import router as health_router
from app.api.metrics import router as metrics_router

app = FastAPI(title="Operational Metrics API")

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(health_router, prefix="/health", tags=["Health"])
app.include_router(metrics_router, prefix="/metrics", tags=["Metrics"])