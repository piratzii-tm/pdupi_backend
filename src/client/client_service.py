from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from src.client.client_repository import ClientRepository
from src.client.client_model import ClientModel
from hashlib import sha256
from typing import Optional
from fastapi import Depends, HTTPException


class ClientService:
    def __init__(self):
        self.client_repository = ClientRepository()

    def get_client_by_id(self, user_id: int) -> ClientModel:
        return self.client_repository.get_client_by_id(received_id=user_id)

    def get_client_by_email(self, user_email: str) -> ClientModel:
        return self.client_repository.get_client_by_email(received_email=user_email)

    def login_client(self, login_info: OAuth2PasswordRequestForm = Depends()) -> Optional[ClientModel]:
        user = self.get_client_by_email(user_email=login_info.username)
        hashed_password = sha256(str.encode(login_info.password)).hexdigest()

        if not user or user.password != hashed_password:
            return None

        return user

    def register_client(self, user_data: ClientModel):
        self.client_repository.register_client(new_user=user_data)