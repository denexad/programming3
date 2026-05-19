from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.models import Category, Order, OrderItem, Product, Profile, User


async def seed_database(session: AsyncSession) -> None:
    existing_user = await session.scalar(select(User).where(User.username == "admin"))
    if existing_user is not None:
        return

    admin = User(
        username="admin",
        email="admin@example.com",
        hashed_password=hash_password("admin123"),
        profile=Profile(
            first_name="Admin",
            last_name="User",
            phone="+380501112233",
            address="Kyiv",
        ),
    )
    student = User(
        username="student",
        email="student@example.com",
        hashed_password=hash_password("student123"),
        profile=Profile(
            first_name="Student",
            last_name="Tester",
            phone="+380671112233",
            address="Lviv",
        ),
    )

    electronics = Category(name="Electronics", description="Useful tech devices")
    books = Category(name="Books", description="Study and reference books")

    laptop = Product(
        name="Laptop",
        description="FastAPI development laptop",
        price=Decimal("35000.00"),
        category=electronics,
    )
    keyboard = Product(
        name="Keyboard",
        description="Mechanical keyboard",
        price=Decimal("2500.00"),
        category=electronics,
    )
    fastapi_book = Product(
        name="FastAPI Book",
        description="Backend development guide",
        price=Decimal("750.00"),
        category=books,
    )

    order = Order(
        user=student,
        status="created",
        items=[
            OrderItem(product=laptop, quantity=1, unit_price=laptop.price),
            OrderItem(product=fastapi_book, quantity=2, unit_price=fastapi_book.price),
        ],
    )

    session.add_all([admin, student, electronics, books, laptop, keyboard, fastapi_book, order])
    await session.commit()
