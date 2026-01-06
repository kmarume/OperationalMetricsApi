from fastapi import FastAPI
from app.api import health, metrics

app = FastAPI()

app.include_router(health.router)
app.include_router(metrics.router)

@app.get("/")
def greet():
    return "test"