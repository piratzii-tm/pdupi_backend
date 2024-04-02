from hashlib import sha256

from fastapi import HTTPException, APIRouter
from src.client.client_model import ClientModel, ClientBase
from src.client.client_service import ClientService
from constants.models.login_info import LoginInfo

client_router = APIRouter(prefix='/client', tags=["product"])
client_service = ClientService()


@client_router.get('/{id}')
def get_user_by_id(user_id: int):
    user = client_service.get_client_by_id(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="No user found at that id")

    return user


@client_router.post('/login')
async def login(login_info: LoginInfo):
    user = client_service.login_client(login_info)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    return {"access_token": user.email, "token_type": "bearer"}


@client_router.post("/register")
async def register(client_base: ClientBase):
    unhashed_password = client_base.password
    client_base.password = sha256(str.encode(client_base.password)).hexdigest()
    client_service.register_client(ClientModel(**client_base.dict()))

    login_info = LoginInfo(**{
        "email": client_base.email,
        "password": unhashed_password
    })

    user = client_service.login_client(login_info)

    if not user:
        raise HTTPException(status_code=400, detail="Something went wrong on register")

    return {"access_token": user.email, "token_type": "bearer"}
