from fastapi import FastAPI

from app.api.users import router as users_router

app = FastAPI(
    title="FastAPI Template",
    version="0.1.0",
)

app.include_router(users_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "FastAPI template is running"}
