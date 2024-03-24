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
