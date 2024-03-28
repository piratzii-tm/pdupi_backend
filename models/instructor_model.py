from sqlalchemy import String, Column, Integer
from pydantic import BaseModel
from database import Base


class InstructorModel(Base):
    __tablename__ = 'instructors'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    hire_date = Column(String(100), nullable=False)


class InstructorBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    hire_date: str
    working_gym_id: int
