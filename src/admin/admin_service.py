from src.admin.admin_repository import AdminRepository
from src.gym_class.gym_class_model import GymClassModel
from src.calendar_day.calendar_day_model import CalendarDayModel
from src.admin.admin_model import AdminModel
from src.instructor.instructor_model import InstructorModel
from fastapi.security import OAuth2PasswordRequestForm
from hashlib import sha256
from typing import Optional
from fastapi import Depends

class AdminService:
    def __init__(self):
        self.admin_repository = AdminRepository()

    def add_class(self, calendar_day: CalendarDayModel, gym_class: GymClassModel):
        self.admin_repository.add_class(calendar_day, gym_class)

    def get_admin_by_email(self, user_email: str) -> AdminModel:
        return self.admin_repository.get_admin_by_email(user_email)

    def login_admin(self, login_info: OAuth2PasswordRequestForm = Depends()) -> Optional[AdminModel]:
        user = self.get_admin_by_email(user_email=login_info.username)
        hashed_password = sha256(str.encode(login_info.password)).hexdigest()

        if not user or user.password != hashed_password:
            return None

        return user

    def add_trainer(self, instructor: InstructorModel):
        self.admin_repository.add_trainer(instructor)