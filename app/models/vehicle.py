from datetime import datetime

from sqlalchemy import Column, Date, DateTime, Integer, String

from app.db.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)

    vehicle_number = Column(String(20), unique=True, nullable=False)
    vehicle_type = Column(String(50), nullable=False)

    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)

    fuel_type = Column(String(30), nullable=False)

    capacity = Column(Integer, nullable=False)

    status = Column(
        String(30),
        default="Active"
    )

    last_service_date = Column(Date)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )