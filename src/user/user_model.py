from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel


class UserModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String(256), nullable=False)


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
