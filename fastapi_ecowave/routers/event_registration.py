from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.event_registration import EventRegistration
from schemas.event_registration import EventRegistrationCreate, EventRegistrationOut

router = APIRouter(prefix="/registrations", tags=["Registrations"])

@router.post("/", response_model=EventRegistrationOut,  status_code=status.HTTP_200_OK)
def create_registration(data: EventRegistrationCreate, db: Session = Depends(get_db)):
    reg = EventRegistration(**data.dict())
    db.add(reg)
    db.commit()
    db.refresh(reg)
    return reg

@router.get("/", response_model=list[EventRegistrationOut], status_code=status.HTTP_200_OK)
def get_registrations(db: Session = Depends(get_db)):
    return db.query(EventRegistration).all()

@router.get("/{reg_id}", response_model=EventRegistrationOut, status_code=status.HTTP_200_OK)
def get_registration(reg_id: int, db: Session = Depends(get_db)):
    reg = db.query(EventRegistration).filter(EventRegistration.reg_id == reg_id).first()
    if reg is None:
        return {"detail": f"Registration with ID {reg_id} not found"}
    return reg

@router.delete("/{reg_id}", status_code=status.HTTP_200_OK)
def delete_registration(reg_id: int, db: Session = Depends(get_db)):
    reg = db.query(EventRegistration).filter(EventRegistration.reg_id == reg_id).first()
    if reg is None:
        return {"detail": f"Registration with ID {reg_id} not found"}
        
    db.delete(reg)
    db.commit()
    return {"message": "Registration deleted"}