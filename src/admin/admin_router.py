import datetime

from fastapi import APIRouter, Depends, HTTPException
from src.admin.admin_service import AdminService
from src.calendar_day.calendar_day_model import CalendarDayModel
from src.gym_class.gym_class_model import GymClassModel
from src.instructor.instructor_model import InstructorModel
from constants.models.add_class_body import AddClassBody
from constants.models.add_trainer_body import AddTrainerBody
from constants.helpers.jwt_handlers import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_admin
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from datetime import date

admin_router = APIRouter(prefix="/admin", tags=["products"])
admin_service = AdminService()


@admin_router.post("/")
async def me(current_user_token: dict = Depends(get_current_admin)):
    return admin_service.get_admin_by_email(current_user_token["sub"])


@admin_router.post("/login")
async def login(login_info: OAuth2PasswordRequestForm = Depends()):
    admin = admin_service.login_admin(login_info)

    if not admin:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": admin.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@admin_router.post("/add_trainer")
async def add_trainer(body: AddTrainerBody):
    admin_service.add_trainer(InstructorModel(**{
        "first_name": body.first_name,
        "last_name": body.last_name,
        "email": f"{body.last_name.lower()}.{body.first_name.lower()}@gymfit.ro",
        "password": "GymFit2024",
        "hire_date": date.today()
    }))


@admin_router.post("/add_class")
async def add_class(body: AddClassBody):
    admin_service.add_class(CalendarDayModel(**{
        "day": body.day,
        "month": body.month,
        "starting_hour": body.starting_hour,
        "class_id": -1
    }), GymClassModel(**{
        "class_name": body.class_name,
        "instructor_id": body.instructor_id,
        "max_slots": body.max_slots,
        "occupied_slots": 0
    }))
