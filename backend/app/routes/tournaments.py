from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database
from datetime import datetime

router = APIRouter(prefix="/tournaments", tags=["Tournaments"])

@router.post("/")
def create_tournament(name: str, date: datetime, type: str, max_teams: int, players_per_team: int, db: Session = Depends(database.SessionLocal)):
    tour = models.Tournament(name=name, date=date, type=type, max_teams=max_teams, players_per_team=players_per_team)
    db.add(tour)
    db.commit()
    return tour

@router.get("/")
def list_tournaments(db: Session = Depends(database.SessionLocal)):
    return db.query(models.Tournament).all()
