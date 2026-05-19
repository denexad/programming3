from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Template",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "FastAPI template is running"}
