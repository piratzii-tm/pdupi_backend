from sqlalchemy import Column, Boolean, String, Integer
from models.user_model import UserModel, UserBase


class ClientModel(UserModel):
    __tablename__ = "clients"

    __mapper_args__ = {
        'polymorphic_identity': 'comment',
        'inherit_condition': (id == UserModel.id),
    }

    id = Column(Integer)
    is_active = Column(Boolean)
    created_at = Column(String(100))
    updated_at = Column(String(100))


class ClientBase(UserBase):
    is_active: bool
    created_at: str
    updated_at: str
