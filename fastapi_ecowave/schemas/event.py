from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class EventBase(BaseModel):
    event_name: str
    event_description: Optional[str] = None
    event_date: datetime
    location_name: str
    event_category: str
    status: str

class EventCreate(EventBase):
    user_id: int

class EventOut(EventBase):
    event_id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)
