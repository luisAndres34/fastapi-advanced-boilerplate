from sqlmodel import Field
from .base import BaseModel
from .enums import UserRole

class User(BaseModel, table=True):
    email: str = Field(unique=True, index=True)
    hashed_password: str
    name: str
    role: UserRole = Field(default=UserRole.user)
    is_active: bool = Field(default=True)
