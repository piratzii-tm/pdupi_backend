from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from pydantic import BaseModel


class CalendarDayModel(Base):
    __tablename__ = 'calendar_days'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    class_id = Column(Integer, ForeignKey("gym_classes.id"), primary_key=True)
    day = Column(Integer, nullable=False)
    starting_hour = Column(Integer, nullable=False)
    ending_hour = Column(Integer, nullable=False)
    date = Column(String, nullable=False)


class CalendarDayBase(BaseModel):
    class_id: int
    day: int
    starting_hour: int
    ending_hour: int
    date: str
