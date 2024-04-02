from sqlalchemy import Column, Boolean, String
from src.user.user_model import UserModel, UserBase


class AdminModel(UserModel):
    __tablename__ = "admin"

    is_active = Column(Boolean, nullable=False)
    created_at = Column(String(100), nullable=False)
    updated_at = Column(String(100), nullable=False)


class AdminBase(UserBase):
    is_active: bool
    created_at: str
    updated_at: str
