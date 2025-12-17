from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.temp import Temp
from schemas.temp import TempBase
from dependencies import get_db

router = APIRouter(prefix="/temp", tags=["Tempereavry"])\

@router.post("/")
def create_temp(data:TempBase,  db:Session=Depends(get_db)):
    new_entry = Temp(
        id = data.id,
        name =data.name
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

