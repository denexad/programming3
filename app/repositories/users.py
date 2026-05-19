from app.schemas.user import UserRead

users_storage: dict[int, UserRead] = {
    1: UserRead(
        id=1,
        username="admin",
        full_name="Admin User",
        age=21,
    )
}
