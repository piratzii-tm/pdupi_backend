from sqlalchemy import Column, Boolean, String, Integer
from pydantic import BaseModel
from database import Base


class ClientModel(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean, nullable=False)
    created_at = Column(String(100), nullable=False)
    updated_at = Column(String(100), nullable=False)


class ClientBase(BaseModel):

    first_name: str
    last_name: str
    email: str
    password: str
    is_active: bool
    created_at: str
    updated_at: str