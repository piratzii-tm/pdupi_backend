from fastapi.security import OAuth2PasswordRequestForm

from src.client.client_repository import ClientRepository
from src.client.client_model import ClientModel
from src.user.user_model import UserModel
from src.reservation.reservation_model import ReservationModel
from hashlib import sha256
from typing import Optional
from fastapi import Depends
from datetime import date


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

        self.client_repository.login_client(user.id)
        return user

    def register_client(self, user_data: ClientModel):
        return self.client_repository.register_client(new_user=user_data)

    def get_all_clients(self):
        return self.client_repository.get_all_clients()

    def get_all_classes(self, received_id: int):
        return self.client_repository.get_all_classes(received_id=received_id)

    def join_class(self, reservation: ReservationModel):
        return self.client_repository.join_class(reservation)

    def exit_class(self, reservation: ReservationModel):
        self.client_repository.exit_class(reservation)
