from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.api.deps import get_current_user
from app.db.session import get_session
from app.models import Order, OrderItem, Product, User
from app.schemas.order import OrderCreate, OrderRead

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/", response_model=list[OrderRead])
async def get_orders(session: AsyncSession = Depends(get_session)) -> list[Order]:
    orders = await session.scalars(
        select(Order).options(selectinload(Order.items)).order_by(Order.id)
    )
    return list(orders)


@router.post("/", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
async def create_order(
    order_data: OrderCreate,
    session: AsyncSession = Depends(get_session),
) -> Order:
    user = await session.get(User, order_data.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    order = Order(user_id=order_data.user_id)
    for item_data in order_data.items:
        product = await session.get(Product, item_data.product_id)
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        order.items.append(
            OrderItem(
                product_id=product.id,
                quantity=item_data.quantity,
                unit_price=product.price,
            )
        )

    session.add(order)
    await session.commit()
    order = await session.scalar(
        select(Order).options(selectinload(Order.items)).where(Order.id == order.id)
    )
    if order is None:
        raise HTTPException(status_code=500, detail="Order was not loaded")
    return order


@router.get("/my", response_model=list[OrderRead])
async def get_my_orders(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> list[Order]:
    orders = await session.scalars(
        select(Order)
        .options(selectinload(Order.items))
        .where(Order.user_id == current_user.id)
        .order_by(Order.id)
    )
    return list(orders)
