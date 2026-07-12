from datetime import datetime

from pydantic import BaseModel


class TripCreate(BaseModel):
    trip_number: str
    vehicle_id: int
    driver_id: int
    source: str
    destination: str
    distance_km: float


class TripResponse(BaseModel):
    id: int
    trip_number: str
    vehicle_id: int
    driver_id: int
    source: str
    destination: str
    distance_km: float
    status: str

    class Config:
        from_attributes = True