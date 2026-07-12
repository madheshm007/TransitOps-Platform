from datetime import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True)

    phone = Column(String(20), nullable=False)

    license_number = Column(String(50), unique=True, nullable=False)

    license_expiry = Column(Date, nullable=False)

    status = Column(String(20), default="Available")

    assigned_vehicle_id = Column(
        Integer,
        ForeignKey("vehicles.id"),
        nullable=True
    )

    vehicle = relationship("Vehicle")

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )