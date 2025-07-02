# Cod-gpt
README.md (starter)

# 🎮 Fullstack Tournament Web App

A containerized full-stack app for managing game tournaments, teams, and user roles (admin, moderator, contestant). Built with React, FastAPI, PostgreSQL, and Discord integration.

## 🔧 Stack
- **Frontend**: React + Tailwind (Vite)
- **Backend**: FastAPI + PostgreSQL + OAuth2
- **Auth**: Manual login + Discord OAuth
- **Database**: PostgreSQL
- **Containerized**: Docker + Compose

## 🚀 Getting Started

### Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Setup
```bash
git clone https://github.com/Rhinofucked/cod-gpt.git
cd fullstack-tournament-app
cp .env.example .env
# Edit your Discord credentials, DB settings, etc.

# Build and run the stack
docker-compose up --build

Visit:

Frontend: http://localhost:5173

Backend API: http://localhost:8000/docs (with Swagger UI)


🧪 Testing

Tests and CI setup coming soon.

✨ Features

Discord OAuth + manual login

Role-based permissions

Tournament creation + team assignment by skill level

Game stat tracking by moderators

Result posting to Discord via Webhooks
