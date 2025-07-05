from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, auth, database

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
def register(username: str, password: str, discord_id: str | None = None, db: Session = Depends(database.SessionLocal)):
    if db.query(models.User).filter_by(username=username).first():
        raise HTTPException(status_code=400, detail="Username taken")
    user = models.User(
        username=username,
        password=auth.get_password_hash(password),
        discord_id=discord_id
    )
    db.add(user)
    db.commit()
    return {"message": "Registered successfully"}

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(database.SessionLocal)):
    user = db.query(models.User).filter_by(username=username).first()
    if not user or not auth.verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
