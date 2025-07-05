import os
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def post_match_result(match, team1, team2, stats):
    if WEBHOOK_URL:
        content = f"Match Result: {team1} defeated {team2} in Tournament {match.tournament_id}."
        requests.post(WEBHOOK_URL, json={"content": content})
