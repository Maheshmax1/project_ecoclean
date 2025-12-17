from pydantic import BaseModel

class TempBase(BaseModel):
    id : int
    name : str
