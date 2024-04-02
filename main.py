<<<<<<< Updated upstream
from fastapi import FastAPI, Depends, status
from typing import Annotated

from models import gym_model, worker_model, user_model, client_model
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

gym_model.GymModel.metadata.create_all(bind=engine)
user_model.UserModel.metadata.create_all(bind=engine)
client_model.ClientModel.metadata.create_all(bind=engine)
worker_model.WorkerModel.metadata.create_all(bind=engine)
=======
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
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
>>>>>>> Stashed changes

app.include_router(client_router)

<<<<<<< Updated upstream
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/create_gym/", status_code=status.HTTP_201_CREATED)
async def create_gym(gym_data: gym_model.GymBase, db: db_dependency):
    db_gym = gym_model.GymModel(**gym_data.dict())
    db.add(db_gym)
    db.commit()
=======
ClientModel.metadata.create_all(bind=engine)
InstructorModel.metadata.create_all(bind=engine)
GymClassModel.metadata.create_all(bind=engine)
CalendarDayModel.metadata.create_all(bind=engine)
ReservationModel.metadata.create_all(bind=engine)
AdminModel.metadata.create_all(bind=engine)
>>>>>>> Stashed changes
