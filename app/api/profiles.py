from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.models import Profile, User
from app.schemas.profile import ProfileCreate, ProfileRead

router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.get("/", response_model=list[ProfileRead])
async def get_profiles(session: AsyncSession = Depends(get_session)) -> list[Profile]:
    profiles = await session.scalars(select(Profile).order_by(Profile.id))
    return list(profiles)


@router.post("/", response_model=ProfileRead, status_code=status.HTTP_201_CREATED)
async def create_profile(
    profile_data: ProfileCreate,
    session: AsyncSession = Depends(get_session),
) -> Profile:
    user = await session.get(User, profile_data.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    existing_profile = await session.scalar(
        select(Profile).where(Profile.user_id == profile_data.user_id)
    )
    if existing_profile is not None:
        raise HTTPException(status_code=409, detail="Profile already exists")

    profile = Profile(**profile_data.model_dump())
    session.add(profile)
    await session.commit()
    await session.refresh(profile)
    return profile
