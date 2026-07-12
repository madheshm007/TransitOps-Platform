from sqlalchemy.orm import Session

from app.repositories.vehicle_repository import (
    create_vehicle,
    delete_vehicle,
    get_all_vehicles,
    get_vehicle,
)
from app.schemas.vehicle import VehicleCreate


def add_vehicle(db: Session, vehicle: VehicleCreate):
    return create_vehicle(db, vehicle)


def list_vehicles(db: Session):
    return get_all_vehicles(db)


def get_vehicle_by_id(db: Session, vehicle_id: int):
    vehicle = get_vehicle(db, vehicle_id)

    if not vehicle:
        raise ValueError("Vehicle not found")

    return vehicle


def remove_vehicle(db: Session, vehicle_id: int):
    vehicle = delete_vehicle(db, vehicle_id)

    if not vehicle:
        raise ValueError("Vehicle not found")

    return {"message": "Vehicle deleted successfully"}