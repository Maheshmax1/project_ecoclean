from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    full_name = Column(String)
    role = Column(String)

    admin = relationship("Admin", back_populates="user", uselist=False)
    volunteer = relationship("Volunteer", back_populates="user", uselist=False)
    registrations = relationship("EventRegistration", back_populates="user")
