from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class ContactMessageCreate(BaseModel):
    sender_name: str
    sender_email: Optional[str] = None
    phone_number: Optional[str] = None
    category: Optional[str] = None
    subject: str
    priority_level: str

class ContactMessageOut(ContactMessageCreate):
    message_id: int
    submission_date: datetime

    model_config = ConfigDict(from_attributes=True)
