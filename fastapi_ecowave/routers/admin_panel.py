from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependencies import get_db

from models.user import User
from models.volunteer import Volunteer
from models.event import Event
from models.contact_message import ContactMessage

from schemas.volunteer import VolunteerOut
from schemas.event import EventCreate, EventOut
from schemas.contact_message import ContactMessageOut

router = APIRouter(
    prefix="/admin-panel",
    tags=["Admin Panel"]
)
@router.get("/dashboard",  status_code=status.HTTP_200_OK)
def dashboard(db: Session = Depends(get_db)):
    return {
        "total_users": db.query(User).count(),
        "total_volunteers": db.query(Volunteer).count(),
        "total_events": db.query(Event).count(),
        "total_messages": db.query(ContactMessage).count()
    }

@router.get("/volunteers", response_model=list[VolunteerOut],  status_code=status.HTTP_200_OK)
def get_volunteers(db: Session = Depends(get_db)):
    return db.query(Volunteer).all()


@router.get("/volunteers/{user_id}", response_model=VolunteerOut,  status_code=status.HTTP_200_OK)
def get_volunteer(user_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunteer).filter(Volunteer.user_id == user_id).first()
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    return volunteer
@router.get("/events", response_model=list[EventOut],  status_code=status.HTTP_200_OK)
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).all()


@router.post("/events", response_model=EventOut,  status_code=status.HTTP_200_OK)
def create_event(data: EventCreate, db: Session = Depends(get_db)):
    event = Event(**data.dict())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.put("/events/{event_id}", response_model=EventOut,  status_code=status.HTTP_200_OK)
def update_event(event_id: int, data: EventCreate, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.event_id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    for key, value in data.dict().items():
        setattr(event, key, value)

    db.commit()
    return event


@router.delete("/events/{event_id}",  status_code=status.HTTP_200_OK)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.event_id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(event)
    db.commit()
    return {"message": "Event deleted"}
@router.get("/messages", response_model=list[ContactMessageOut] , status_code=status.HTTP_200_OK)
def get_messages(db: Session = Depends(get_db)):
    return db.query(ContactMessage).order_by(
        ContactMessage.submission_date.desc()
    ).all()
