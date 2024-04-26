from fastapi import APIRouter, HTTPException
from src.instructor.instructor_service import InstructorService

instructor_router = APIRouter(prefix="/trainer", tags=["product"])
instructor_service = InstructorService()


@instructor_router.get("/")
async def get_instructor_by_id(instructor_id: int):
    instructor =  instructor_service.get_instructor(instructor_id=instructor_id)

    if not instructor:
        raise HTTPException(status_code=404, detail="No instructor with that id.")

    return instructor


@instructor_router.get("/all")
async def get_all_instructors():
    instructors =  instructor_service.get_instructor()

    if not instructors:
        raise HTTPException(status_code=404, detail="No instructors.")

    return instructors