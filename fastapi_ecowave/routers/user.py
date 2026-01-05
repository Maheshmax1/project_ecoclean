from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.user import User
from schemas.user import UserCreate, UserOut

router = APIRouter(prefix="/users", tags=["Users"])



@router.post("/", response_model=UserOut,  status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    user = User(email=data.email, full_name=data.full_name, role=data.role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/", response_model=list[UserOut],  status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{user_id}", response_model=UserOut, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        return {"detail": f"User with ID {user_id} not found"}
    return user

@router.put("/{user_id}", response_model=UserOut,  status_code=status.HTTP_200_OK)
def update_user(user_id: int, data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        return {"detail": f"User with ID {user_id} not found"}
    
    for key, value in data.dict().items():
        setattr(user, key, value)
        
    db.commit()
    return user

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        return {"detail": f"User with ID {user_id} not found"}
        
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}

@router.get("/", response_model=list[UserOut],  status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()