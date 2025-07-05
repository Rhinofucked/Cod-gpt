from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database, discord

router = APIRouter(prefix="/matches", tags=["Matches"])

@router.post("/")
def report_match(tournament_id: int, winner: str, db: Session = Depends(database.SessionLocal)):
    match = models.Match(tournament_id=tournament_id, winner=winner)
    db.add(match)
    db.commit()
    discord.post_match_result(match, team1=winner, team2="TBD", stats=[])
    return {"message": "Match reported"}
