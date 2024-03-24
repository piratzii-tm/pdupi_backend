from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.user_model import UserModel, UserBase


class WorkerModel(UserModel):
    __tablename__ = 'workers'

    __mapper_args__ = {
        'polymorphic_identity': 'comment',
        'inherit_condition': (id == UserModel.id),
    }

    id = Column(Integer)
    hire_date = Column(String(100))
    working_gym_id = Column(Integer, ForeignKey("gyms.id"), primary_key=True)
    gym = relationship("GymModel", back_populates="workers")


class WorkerBase(UserBase):
    hire_date: str
    working_gym_id: id
