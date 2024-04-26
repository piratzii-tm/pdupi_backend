from fastapi import APIRouter
from src.instructor.instructor_service import InstructorService

instructor_router = APIRouter(prefix="/trainer", tags=["product"])
instructor_service = InstructorService()


@instructor_router.get("/")
async def get_instructor_by_id(instructor_id: int):
    return instructor_service.get_instructor(instructor_id=instructor_id)


@instructor_router.get("/all")
async def get_all_instructors():
    return instructor_service.get_instructor()