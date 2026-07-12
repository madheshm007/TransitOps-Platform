from datetime import date

from pydantic import BaseModel, EmailStr


class DriverCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    license_number: str
    license_expiry: date
    assigned_vehicle_id: int | None = None


class DriverResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str
    license_number: str
    status: str

    class Config:
        from_attributes = True