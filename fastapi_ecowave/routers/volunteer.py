
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.volunteer import Volunteer
from schemas.volunteer import VolunteerCreate, VolunteerOut

router = APIRouter(prefix="/volunteers", tags=["Volunteers"])


@router.post("/", response_model=VolunteerOut,  status_code=status.HTTP_200_OK)
def create_volunteer(data: VolunteerCreate, db: Session = Depends(get_db)):
    new_entry = Volunteer(
        user_id=data.user_id,  
        phone_number=data.phone_number,
        age_group=data.age_group,
        area_of_interest=data.area_of_interest,        
        motivation_message=data.motivation_message     
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry


@router.get("/", response_model=list[VolunteerOut],  status_code=status.HTTP_200_OK)
def get_volunteers(db: Session = Depends(get_db)):
    return db.query(Volunteer).all()


@router.get("/{user_id}", response_model=VolunteerOut,  status_code=status.HTTP_200_OK)
def get_volunteer(user_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunteer).filter(Volunteer.user_id == user_id).first()
    if volunteer is None:
        raise HTTPException(
            status_code=404,
            detail=f"Volunteer record for User ID {user_id} not found"
        )
    return volunteer


@router.put("/{user_id}", response_model=VolunteerOut,  status_code=status.HTTP_200_OK)
def update_volunteer(user_id: int, data: VolunteerCreate, db: Session = Depends(get_db)):
    volunteer = db.query(Volunteer).filter(Volunteer.user_id == user_id).first()
    if volunteer is None:
        raise HTTPException(
            status_code=404,
            detail=f"Volunteer record for User ID {user_id} not found"
        )

    for key, value in data.dict().items():
        setattr(volunteer, key, value)

    db.commit()
    db.refresh(volunteer)
    return volunteer


@router.delete("/{user_id}",  status_code=status.HTTP_200_OK)
def delete_volunteer(user_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunteer).filter(Volunteer.user_id == user_id).first()
    if volunteer is None:
        raise HTTPException(
            status_code=404,
            detail=f"Volunteer record for User ID {user_id} not found"
        )

    db.delete(volunteer)
    db.commit()
    return {"message": "Volunteer deleted"}
