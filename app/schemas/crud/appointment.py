from pydantic import BaseModel
from uuid import UUID


class Appointment(BaseModel):
    client_id: UUID
    provider_schedule_id: UUID
    is_confirmed: bool = False
    is_expired: bool = False


class AppointmentCreate(Appointment):
    pass
