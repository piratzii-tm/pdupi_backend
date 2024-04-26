from sqlalchemy import Column, Boolean

from src.user.user_model import UserModel, UserBase


class AdminModel(UserModel):
    __tablename__ = "admin"

    topg = Column(Boolean, nullable=True)


class AdminBase(UserBase):
    topg: bool
