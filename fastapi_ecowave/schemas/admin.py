from pydantic import BaseModel, ConfigDict
from schemas.user import UserOut

class AdminCreate(BaseModel):
    user_id: int

class AdminOut(BaseModel):
    admin_id: int
    user: UserOut

    model_config = ConfigDict(from_attributes=True)
