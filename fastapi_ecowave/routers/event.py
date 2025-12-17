from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.event import Event
from schemas.event import EventCreate, EventOut

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/", response_model=EventOut,  status_code=status.HTTP_200_OK)
def create_event(data: EventCreate, db: Session = Depends(get_db)):
    event = Event(**data.dict())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

@router.get("/", response_model=list[EventOut], status_code=status.HTTP_200_OK)
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).all()

@router.get("/{event_id}", response_model=EventOut, status_code=status.HTTP_200_OK)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.event_id == event_id).first()
    if event is None:
        return {"detail": f"Event with ID {event_id} not found"}
    return event

@router.put("/{event_id}", response_model=EventOut, status_code=status.HTTP_200_OK)
def update_event(event_id: int, data: EventCreate, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.event_id == event_id).first()
    if event is None:
        return {"detail": f"Event with ID {event_id} not found"}
        
    for key, value in data.dict().items():
        setattr(event, key, value)
        
    db.commit()
    return event

@router.delete("/{event_id}", status_code=status.HTTP_200_OK)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.event_id == event_id).first()
    if event is None:
        return {"detail": f"Event with ID {event_id} not found"}
        
    db.delete(event)
    db.commit()
    return {"message": "Event deleted"}