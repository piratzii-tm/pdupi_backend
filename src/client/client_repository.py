from database import get_db
from src.client.client_model import ClientModel
from src.gym_class.gym_class_model import GymClassModel
from src.reservation.reservation_model import ReservationModel
from src.calendar_day.calendar_day_model import CalendarDayModel
from typing import List
from datetime import date


class ClientRepository:
    def __init__(self):
        self.db = next(get_db())

    def get_client_by_id(self, received_id: int) -> ClientModel:
        return self.db.query(ClientModel) \
            .filter(ClientModel.id == received_id) \
            .first()

    def get_client_by_email(self, received_email: str) -> ClientModel:
        return self.db.query(ClientModel) \
            .filter(ClientModel.email == received_email) \
            .first()

    def register_client(self, new_user: ClientModel):
        users: List[ClientModel] = self.db.query(ClientModel).where(ClientModel.email == new_user.email).all()
        if len(users) == 0:
            self.db.add(new_user)
            self.db.commit()
            return True
        return False

    def get_all_clients(self):
        clients: List[ClientModel] = self.db.query(ClientModel).all()
        return clients

    def get_all_classes(self, received_id: int):
        client_reservations: List[ReservationModel] = self.db.query(ReservationModel) \
            .filter(ReservationModel.client_id == received_id)

        classes = []

        for reservation in client_reservations:
            classes.append(
                {
                    "class": self.db.query(GymClassModel).filter(GymClassModel.id == reservation.class_id).first(),
                    "day": self.db.query(CalendarDayModel).filter(CalendarDayModel.id == reservation.day_id).first()
                }
            )

        return classes

    def join_class(self, reservation: ReservationModel):
        users_reservations: List[ReservationModel] = self.db.query(ReservationModel).where(
            ReservationModel.client_id == reservation.client_id and
            ReservationModel.class_id == reservation.class_id and
            ReservationModel.day_id == reservation.day_id
        ).all()
        if len(users_reservations) == 0:
            self.db.add(reservation)
            self.db.commit()
            return True
        return False

    def exit_class(self, reservation: ReservationModel):
        self.db.query(ReservationModel).where(
            ReservationModel.client_id == reservation.client_id and
            ReservationModel.class_id == reservation.class_id and
            ReservationModel.day_id == reservation.day_id
        ).delete()
        self.db.commit()

    def login_client(self, user_id: int):
        client = self.db.query(ClientModel).where(ClientModel.id == user_id).first()
        print("Hello1")
        if client:
            print("Hello2")
            setattr(client, "updated_at", date.today())
            self.db.commit()
            self.db.refresh(client)

