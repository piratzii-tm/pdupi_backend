from sqlalchemy import Column, Boolean, String

from src.user.user_model import UserBase, UserModel


class ClientModel(UserModel):
    __tablename__ = "client"

    is_active = Column(Boolean, nullable=False)
    created_at = Column(String(200), nullable=False)
    updated_at = Column(String(200), nullable=False)


class ClientBase(UserBase):
    is_active: bool
    created_at: str
    updated_at: str
