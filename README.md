# FastAPI Template

Template project for a FastAPI application managed with Poetry.

## Requirements

- Python 3.12+
- Poetry

## Install

```bash
poetry install
```

## Run

```bash
poetry run uvicorn app.main:app --reload
```

The application starts at `http://127.0.0.1:8000`.

## Users API

- `GET /users/` - get all users.
- `GET /users/{user_id}` - get user by id.
- `POST /users/` - create user.
- `PUT /users/{user_id}` - update user.
- `DELETE /users/{user_id}` - delete user.

## Auth API

- `POST /auth/register` - register a user.
- `POST /auth/login` - authenticate and receive a JWT cookie.
- `GET /auth/me` - get current authenticated user.
- `GET /auth/me/profile` - get current authenticated user's profile.
- `POST /auth/logout` - clear JWT cookie.

## Docker

```bash
docker compose up --build
```

Docker Compose starts two containers:

- `api` - FastAPI application with auto reload enabled.
- `db` - PostgreSQL database.

The project folder is mounted into `/app` inside the API container.
Open the Docker version at `http://127.0.0.1:8001`.
