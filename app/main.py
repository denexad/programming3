from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.categories import router as categories_router
from app.api.orders import router as orders_router
from app.api.products import router as products_router
from app.api.profiles import router as profiles_router
from app.api.users import router as users_router
from app.db.seed import seed_database
from app.db.session import async_session_factory


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    async with async_session_factory() as session:
        await seed_database(session)
    yield

app = FastAPI(
    title="FastAPI Template",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(profiles_router)
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(orders_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "FastAPI template is running"}
