from pydantic import BaseModel, ConfigDict, Field


class ProfileBase(BaseModel):
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    phone: str | None = Field(default=None, max_length=20)
    address: str | None = Field(default=None, max_length=255)


class ProfileCreate(ProfileBase):
    user_id: int


class ProfileRead(ProfileBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)
