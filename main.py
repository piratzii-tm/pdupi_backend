from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from database import engine

from src.instructor.instructor_model import InstructorModel
from src.client.client_model import ClientModel
from src.calendar_day.calendar_day_model import CalendarDayModel
from src.reservation.reservation_model import ReservationModel
from src.gym_class.gym_class_model import GymClassModel
from src.admin.admin_model import AdminModel

from src.client.client_router import client_router
from src.admin.admin_router import admin_router
from src.gym_class.gym_class_router import gym_class_router
from src.instructor.instructor_router import instructor_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

routers = [
    client_router, admin_router, gym_class_router, instructor_router
]

models = [
    ClientModel,
    InstructorModel,
    GymClassModel,
    CalendarDayModel,
    ReservationModel,
    AdminModel
]

for router in routers:
    app.include_router(router)

for model in models:
    model.metadata.create_all(bind=engine)
