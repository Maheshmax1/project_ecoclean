from fastapi import APIRouter, Depends , status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.admin import Admin
from schemas.admin import AdminCreate, AdminOut

router = APIRouter(prefix="/admins", tags=["Admins"])

@router.post("/", response_model=AdminOut,  status_code=status.HTTP_200_OK)
def create_admin(data: AdminCreate, db: Session = Depends(get_db)):
    admin = Admin(user_id=data.user_id)
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

@router.get("/", response_model=list[AdminOut],  status_code=status.HTTP_200_OK)
def get_admins(db: Session = Depends(get_db)):
    return db.query(Admin).all()

@router.get("/{admin_id}", response_model=AdminOut,  status_code=status.HTTP_200_OK)
def get_admin(admin_id: int, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()
    if admin is None:
        return {"detail": f"Admin with ID {admin_id} not found"}
    return admin

@router.delete("/{admin_id}",  status_code=status.HTTP_200_OK)
def delete_admin(admin_id: int, db: Session = Depends(get_db), ):
    admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()
    if admin is None:
        return {"detail": f"Admin with ID {admin_id} not found"}
        
    db.delete(admin)
    db.commit()
    return {"message": "Admin deleted"}