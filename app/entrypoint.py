import subprocess

import uvicorn


def main() -> None:
    subprocess.run(["alembic", "upgrade", "head"], check=True)
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
