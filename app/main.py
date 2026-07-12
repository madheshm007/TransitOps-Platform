from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.vehicle import router as vehicle_router
from app.api.v1.dashboard import router as dashboard_router

app = FastAPI(
    title="TransitOps API",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(vehicle_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {"message": "TransitOps Backend Running 🚚"}