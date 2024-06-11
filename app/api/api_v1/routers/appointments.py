from fastapi import APIRouter, Request, Depends

from app.db.session import get_db
from app.schemas.crud.appointment import AppointmentCreate
from app.crud.appointments import crud_create_appointment
from app.crud.provider_schedules import update_provider_schedule_booking

appointments_router = r = APIRouter()


@r.post(
    "/appointments",
    response_model_exclude_none=True,
)
async def create_client_appointment_reservation(
    request: Request,
    appointment_create: AppointmentCreate,
    db=Depends(get_db),
):
    """
    Create appointment
    """
    created_appointment = crud_create_appointment(db=db, appointment=appointment_create)
    if created_appointment:
        update_provider_schedule_booking(
            db=db,
            provider_schedule_id=appointment_create.provider_schedule_id,
            is_booked=True,
        )
