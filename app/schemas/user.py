from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    full_name: str = Field(min_length=2, max_length=80)
    age: int = Field(ge=1, le=120)


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=3, max_length=30)
    full_name: str | None = Field(default=None, min_length=2, max_length=80)
    age: int | None = Field(default=None, ge=1, le=120)


class UserRead(UserBase):
    id: int
