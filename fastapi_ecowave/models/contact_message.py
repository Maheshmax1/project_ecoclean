from sqlalchemy import Column, Integer, String, TIMESTAMP
from db.database import Base
from datetime import datetime

class ContactMessage(Base):
    __tablename__ = "contact_messages"

    message_id = Column(Integer, primary_key=True, index=True)
    sender_name = Column(String)
    sender_email = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    category = Column(String, nullable=True)
    subject = Column(String)
    priority_level = Column(String)
    submission_date = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
