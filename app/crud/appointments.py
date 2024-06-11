from sqlalchemy.orm import Session

from app.models.appointment import Appointment as AppointmentModel
from app.schemas.crud.appointment import AppointmentCreate


def crud_create_appointment(db: Session, appointment: AppointmentCreate):
    db_client = AppointmentModel(
        provider_schedule_id=appointment.provider_schedule_id,
        client_id=appointment.client_id,
        is_confirmed=appointment.is_confirmed,
        is_expired=appointment.is_expired,
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client
