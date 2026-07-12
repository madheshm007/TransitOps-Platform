from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.vehicle import Vehicle
from app.models.driver import Driver
from app.models.trip import Trip


def get_dashboard_stats(db: Session):

    total_vehicles = db.query(func.count(Vehicle.id)).scalar()

    total_drivers = db.query(func.count(Driver.id)).scalar()

    total_trips = db.query(func.count(Trip.id)).scalar()

    active_vehicles = (
        db.query(func.count(Vehicle.id))
        .filter(Vehicle.status == "Active")
        .scalar()
    )

    maintenance_vehicles = (
        db.query(func.count(Vehicle.id))
        .filter(Vehicle.status == "Maintenance")
        .scalar()
    )

    active_trips = (
        db.query(func.count(Trip.id))
        .filter(Trip.status == "In Progress")
        .scalar()
    )

    return {
        "total_vehicles": total_vehicles,
        "total_drivers": total_drivers,
        "total_trips": total_trips,
        "active_vehicles": active_vehicles,
        "maintenance_vehicles": maintenance_vehicles,
        "active_trips": active_trips,
    }