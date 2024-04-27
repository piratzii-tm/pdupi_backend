from fastapi import APIRouter, HTTPException

from src.gym_class.gym_class_service import GymClassService
from constants.models.gym_class_body import GymClassBody

gym_class_router = APIRouter(prefix="/gym_class", tags=["product"])
gym_class_service = GymClassService()


@gym_class_router.get("/")
async def get_class_by_id(gym_id: int):
    gym_class = gym_class_service.get_gym_class(gym_id=gym_id)
    if not gym_class:
        raise HTTPException(status_code=404, detail="No class with the specified id.")
    return gym_class


@gym_class_router.get("/all")
async def get_all_classes():
    gym_class = gym_class_service.get_gym_class()
    if not gym_class:
        raise HTTPException(status_code=404, detail="No classes.")
    return gym_class


@gym_class_router.post("/filtered")
async def get_class_by_date(body: GymClassBody):
    gym_class =  gym_class_service.get_gym_class(gym_class_body=body)
    if not gym_class:
        raise HTTPException(status_code=404, detail=f"No class in {body.day}.{body.month}")
    return gym_class
