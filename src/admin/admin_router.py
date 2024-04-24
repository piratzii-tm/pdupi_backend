from fastapi import APIRouter

admin_router = APIRouter(prefix="/admin", tags=["products"])
# TODO Add admin service here

@admin_router.post("/")
async def me():
    print("Implement logic")


@admin_router.get("/{id}")
async def get_admin_by_id():
    print("Implement logic")


@admin_router.post("/login")
async def login():
    print("Implement logic")


@admin_router.post("/trainer/add")
async def add_trainer():
    print("Implement logic")


@admin_router.post("/class/add")
async def add_class():
    print("Implement logic")
