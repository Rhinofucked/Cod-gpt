from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database, logic

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.post("/assign")
def assign_teams(tournament_id: int, db: Session = Depends(database.SessionLocal)):
    tournament = db.query(models.Tournament).get(tournament_id)
    users = db.query(models.User).all()
    teams = logic.matchmaking.assign_teams(users, tournament.players_per_team)
    created = []
    for i, group in enumerate(teams):
        team = models.Team(name=f"Team {i+1}", tournament_id=tournament.id)
        db.add(team)
        db.commit()
        created.append(team)
    return created
