from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime

class EventRegistration(Base):
    __tablename__ = "event_registrations"

    reg_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    event_id = Column(Integer, ForeignKey("events.event_id"))
    registration_date = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="registrations")
    event = relationship("Event", back_populates="registrations")
