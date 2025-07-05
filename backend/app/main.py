from fastapi import FastAPI
from .routes import users, tournaments, teams, matches, admin

app = FastAPI()

app.include_router(users.router)
app.include_router(tournaments.router)
app.include_router(teams.router)
app.include_router(matches.router)
app.include_router(admin.router)
