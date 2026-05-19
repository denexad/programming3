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

## Docker

```bash
docker compose up --build
```

Docker Compose starts two containers:

- `api` - FastAPI application with auto reload enabled.
- `db` - PostgreSQL database.

The project folder is mounted into `/app` inside the API container.
Open the Docker version at `http://127.0.0.1:8001`.
