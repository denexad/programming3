from fastapi import APIRouter, HTTPException, status

from app.repositories.users import users_storage
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserRead])
def get_users() -> list[UserRead]:
    return list(users_storage.values())


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int) -> UserRead:
    user = users_storage.get(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate) -> UserRead:
    user_id = max(users_storage.keys(), default=0) + 1
    new_user = UserRead(id=user_id, **user.model_dump())
    users_storage[user_id] = new_user

    return new_user


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_update: UserUpdate) -> UserRead:
    user = users_storage.get(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    updated_user = user.model_copy(update=user_update.model_dump(exclude_unset=True))
    users_storage[user_id] = updated_user

    return updated_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int) -> None:
    if user_id not in users_storage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    del users_storage[user_id]
