from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.contact_message import ContactMessage
from schemas.contact_message import ContactMessageCreate, ContactMessageOut

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.post("/", response_model=ContactMessageOut,  status_code=status.HTTP_200_OK)
def create_message(data: ContactMessageCreate, db: Session = Depends(get_db)):
    msg = ContactMessage(**data.dict())
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg

@router.get("/", response_model=list[ContactMessageOut],  status_code=status.HTTP_200_OK)
def get_messages(db: Session = Depends(get_db)):
    return db.query(ContactMessage).all()

@router.get("/{message_id}", response_model=ContactMessageOut,  status_code=status.HTTP_200_OK)
def get_message(message_id: int, db: Session = Depends(get_db)):
    msg = db.query(ContactMessage).filter(ContactMessage.message_id == message_id).first()
    if msg is None:
        return {"detail": f"Contact message with ID {message_id} not found"}
    return msg

@router.delete("/{message_id}", status_code=status.HTTP_200_OK)
def delete_message(message_id: int, db: Session = Depends(get_db)):
    msg = db.query(ContactMessage).filter(ContactMessage.message_id == message_id).first()
    if msg is None:
        return {"detail": f"Contact message with ID {message_id} not found"}
        
    db.delete(msg)
    db.commit()
    return {"message": "Message deleted"}