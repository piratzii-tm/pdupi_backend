from fastapi import APIRouter

instructor_router = APIRouter(prefix="/trainer", tags=["product"])


# TODO Add instructor service


@instructor_router.get("/")
async def get_instructor_by_id(id: int):
    print("Implement logic")


@instructor_router.get("/all")
async def get_all_instructors():
    print("Implement logic")
