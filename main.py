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

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(client_router)

ClientModel.metadata.create_all(bind=engine)
InstructorModel.metadata.create_all(bind=engine)
GymClassModel.metadata.create_all(bind=engine)
CalendarDayModel.metadata.create_all(bind=engine)
ReservationModel.metadata.create_all(bind=engine)
AdminModel.metadata.create_all(bind=engine)


