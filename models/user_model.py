from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(100), nullable=False)
    las_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)


class UserBase(BaseModel):
    id: int
    first_name: str
    las_name: str
    email: str
    password: str
