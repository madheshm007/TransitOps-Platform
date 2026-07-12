from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.vehicle import VehicleCreate, VehicleResponse
from app.services.vehicle_service import (
    add_vehicle,
    get_vehicle_by_id,
    list_vehicles,
    remove_vehicle,
)

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


@router.post("", response_model=VehicleResponse)
def create(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return add_vehicle(db, vehicle)


@router.get("", response_model=list[VehicleResponse])
def get_all(db: Session = Depends(get_db)):
    return list_vehicles(db)


@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get(vehicle_id: int, db: Session = Depends(get_db)):
    try:
        return get_vehicle_by_id(db, vehicle_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{vehicle_id}")
def delete(vehicle_id: int, db: Session = Depends(get_db)):
    try:
        return remove_vehicle(db, vehicle_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))