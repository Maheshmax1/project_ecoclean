from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from schemas.user import UserOut

class VolunteerBase(BaseModel):
    phone_number: Optional[str] = None
    age_group: Optional[str] = None
    area_of_interest: Optional[str] = None
    motivation_message: Optional[str] = None

class VolunteerCreate(VolunteerBase):
    user_id: int

class VolunteerOut(VolunteerBase):
    user_id: int
    application_date: datetime
    user: Optional[UserOut]

    model_config = ConfigDict(from_attributes=True)






