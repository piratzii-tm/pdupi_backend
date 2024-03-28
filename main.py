from fastapi import FastAPI, Depends, status
from typing import Annotated
from models import instructor_model, client_model, reservation_model, calendarday_model, gym_class_model
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from controllers import register_client_controller

app = FastAPI()

client_model.ClientModel.metadata.create_all(bind=engine)
instructor_model.InstructorModel.metadata.create_all(bind=engine)
gym_class_model.GymClassModel.metadata.create_all(bind=engine)
calendarday_model.CalendarDayModel.metadata.create_all(bind=engine)
reservation_model.ReservationModel.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/register", status_code=status.HTTP_201_CREATED)
async def create_gym(client: client_model.ClientBase, db: db_dependency):
    register_client_controller.register_client(client, db)
