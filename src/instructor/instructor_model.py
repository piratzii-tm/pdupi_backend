from sqlalchemy import String, Column
from src.user.user_model import UserBase, UserModel


class InstructorModel(UserModel):
    __tablename__ = 'instructors'

    hire_date = Column(String(100), nullable=False)


class InstructorBase(UserBase):
    hire_date: str
