from pydantic import BaseModel, ConfigDict
from datetime import datetime
from schemas.user import UserOut
from schemas.event import EventOut

class EventRegistrationCreate(BaseModel):
    user_id: int
    event_id: int

class EventRegistrationOut(BaseModel):
    reg_id: int
    registration_date: datetime
    user: UserOut
    event: EventOut

    model_config = ConfigDict(from_attributes=True)
