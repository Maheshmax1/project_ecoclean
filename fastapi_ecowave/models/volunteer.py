from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime

class Volunteer(Base):
    __tablename__ = "volunteers"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True, nullable=False)
    phone_number = Column(String(20))
    age_group = Column(String(50))
    area_of_interest = Column(String(100))
    motivation_message = Column(Text)
    application_date = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="volunteer")
