from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/users")
def list_users(db: Session = Depends(database.SessionLocal)):
    return db.query(models.User).all()

@router.put("/users/{user_id}/role")
def change_role(user_id: int, role: str, db: Session = Depends(database.SessionLocal)):
    user = db.query(models.User).get(user_id)
    user.role = role
    db.commit()
    return {"message": "Role updated"}
