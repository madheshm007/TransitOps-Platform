from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)

    trip_number = Column(String(50), unique=True, nullable=False)

    vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=False
    )

    driver_id = Column(
        Integer,
        ForeignKey("drivers.id"),
        nullable=False
    )

    source = Column(String(100), nullable=False)

    destination = Column(String(100), nullable=False)

    distance_km = Column(Float)

    status = Column(
        String(30),
        default="Scheduled"
    )

    start_time = Column(DateTime)

    end_time = Column(DateTime)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    vehicle = relationship("Vehicle")

    driver = relationship("Driver")