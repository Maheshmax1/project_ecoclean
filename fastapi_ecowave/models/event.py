from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.database import Base

class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))  
    event_name = Column(String)
    event_description = Column(String)
    event_date = Column(DateTime)
    location_name = Column(String)
    event_category = Column(String)
    status = Column(String)

    registrations = relationship("EventRegistration", back_populates="event")
