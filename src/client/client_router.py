from fastapi import HTTPException, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta
from hashlib import sha256
from datetime import date

from src.client.client_model import ClientModel
from src.user.user_model import UserBase
from src.client.client_service import ClientService
from src.reservation.reservation_model import ReservationModel

from constants.helpers.jwt_handlers import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_client
from constants.models.client_interaction_class import ClientInteractionClass

client_router = APIRouter(prefix='/client', tags=["product"])
client_service = ClientService()


@client_router.post("/")
async def me(current_user_token: dict = Depends(get_current_client)):
    return client_service.get_client_by_email(current_user_token["sub"])


@client_router.get('/')
def get_client_by_id(user_id: int):
    client = client_service.get_client_by_id(user_id)

    if not client:
        raise HTTPException(status_code=404, detail="No user found at that id")

    return client


@client_router.post('/login')
async def login(login_info: OAuth2PasswordRequestForm = Depends()):
    client = client_service.login_client(login_info)

    if not client:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": client.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@client_router.post("/register")
async def register(client_base: UserBase):
    client_base.password = sha256(str.encode(client_base.password)).hexdigest()
    response = client_service.register_client(ClientModel(**{
        "first_name": client_base.first_name,
        "last_name": client_base.last_name,
        "email": client_base.email,
        "password": client_base.password,
        "is_active": True,
        "created_at": date.today(),
        "updated_at": date.today()
    }))

    if response:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": client_base.email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Email already in use.")


@client_router.get("/all")
async def get_all_clients():
    clients = client_service.get_all_clients()

    if not clients:
        raise HTTPException(status_code=404, detail="There are no users registered.")

    return clients


@client_router.get("/classes")
async def get_all_classes(client_id: int):
    classes = client_service.get_all_classes(client_id)

    if not classes or len(classes) == 0:
        raise HTTPException(status_code=400, detail="User did not registered in any class.")

    return classes


@client_router.post("/join")
async def join_class(body: ClientInteractionClass):
    response = client_service.join_class(ReservationModel(**{
        "client_id": body.client_id,
        "class_id": body.class_id,
        "day_id": body.day_id
    }))

    if not response:
        raise HTTPException(status_code=400, detail="User already joined the class")


@client_router.post("/exit")
async def exit_class(body: ClientInteractionClass):
    client_service.exit_class(ReservationModel(**{
        "client_id": body.client_id,
        "class_id": body.class_id,
        "day_id": body.day_id
    }))
