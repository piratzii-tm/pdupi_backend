from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from pydantic import BaseModel


class GymClassModel(Base):
    __tablename__ = 'gym_classes'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    class_name = Column(String(100), nullable=False)
    instructor_id = Column(Integer, ForeignKey("instructors.id"))
    max_slots = Column(Integer, nullable=False)
    occupied_slots = Column(Integer, nullable=False)


class GymClassBase(BaseModel):
    class_name: str
    instructor_id: str
    max_slots: int
    occupied_slots: int
