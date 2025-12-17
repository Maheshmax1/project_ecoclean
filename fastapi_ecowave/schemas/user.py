from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    email: str
    full_name: str
    role: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    user_id: int

    model_config = ConfigDict(from_attributes=True)
