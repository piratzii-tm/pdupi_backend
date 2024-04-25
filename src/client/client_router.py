from datetime import timedelta
from hashlib import sha256

from fastapi import HTTPException, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.client.client_model import ClientModel, ClientBase
from src.client.client_service import ClientService

from constants.helpers.jwt_handlers import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_user

client_router = APIRouter(prefix='/client', tags=["product"])
client_service = ClientService()


@client_router.post("/")
async def me(current_user_token: dict = Depends(get_current_user)):
    return client_service.get_client_by_email(current_user_token["sub"])


@client_router.get('/{id}')
def get_client_by_id(user_id: int):
    user = client_service.get_client_by_id(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="No user found at that id")

    return user


@client_router.post('/login')
async def login(login_info: OAuth2PasswordRequestForm = Depends()):
    user = client_service.login_client(login_info)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@client_router.post("/register")
async def register(client_base: ClientBase):
    client_base.password = sha256(str.encode(client_base.password)).hexdigest()
    client_service.register_client(ClientModel(**client_base.dict()))

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": client_base.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@client_router.get("/all")
async def get_all_clients():
    print("Implement logic")


@client_router.get("/{id}/classes")
async def get_all_classes():
    print("Implement logic")


@client_router.post("/{id}/classes/{class_id}/join")
async def join_class():
    print("Implement logic")


@client_router.post("/{id}/classes/{class_id}/exit")
async def exit_class():
    print("Implement logic")
