from datetime import date

from pydantic import BaseModel


class VehicleCreate(BaseModel):
    vehicle_number: str
    vehicle_type: str
    brand: str
    model: str
    fuel_type: str
    capacity: int
    last_service_date: date


class VehicleResponse(BaseModel):
    id: int
    vehicle_number: str
    vehicle_type: str
    brand: str
    model: str
    fuel_type: str
    capacity: int
    status: str

    class Config:
        from_attributes = True