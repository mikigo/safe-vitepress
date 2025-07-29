# vitepress-fastapi-auth

A secure documentation solution combining Vitepress frontend with FastAPI backend authentication.

## Features
- **FastAPI Authentication**: JWT-based authentication system with role-based access control
- **Vitepress Integration**: Protected documentation routes with seamless auth flow
- **Secure Access Control**: Granular permission management for documentation pages
- **Modern UI**: Clean, responsive design with built-in dark mode support

## Technical Architecture
- **Frontend**: Vitepress with Vue 3 components
- **Backend**: FastAPI with Pydantic models and SQLAlchemy ORM
- **Authentication**: JWT token-based authentication with secure HTTP-only cookies
- **Database**: SQLite with migrations support

## Setup Instructions

### Prerequisites
- Python 3.10+
- Node.js 16+
- pnpm

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup
```bash
pnpm install
pnpm run docs:dev
```

## Environment Configuration
Create `.env` files in both root and backend directories with the following variables:
- `SECRET_KEY`: JWT secret key
- `DATABASE_URL`: SQLite database path
- `TOKEN_EXPIRE_MINUTES`: JWT token expiration time

## Project Structure
- `/docs`: Vitepress documentation source
- `/backend`: FastAPI authentication backend
- `/docs/.vitepress/components`: Vue components for auth UI
- `/backend/models`: Database models
- `/backend/auth`: Authentication logic

## License
MIT