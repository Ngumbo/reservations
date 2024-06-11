from sqlalchemy.orm import Session
from uuid import UUID

from app.models.provider_schedule import ProviderSchedule as ProviderScheduleModel
from app.schemas.crud.provider_schedule import ProviderScheduleCreate


def crud_create_provider_schedule(
    db: Session, provider_schedule: ProviderScheduleCreate
):
    db_provider_schedule = ProviderScheduleModel(
        provider_id=provider_schedule.provider_id,
        start_time=provider_schedule.start_time,
        end_time=provider_schedule.end_time,
        is_booked=provider_schedule.is_booked,
    )
    db.add(db_provider_schedule)
    db.commit()
    db.refresh(db_provider_schedule)

    return db_provider_schedule


def crud_get_provider_schedule(db: Session, provider_id: UUID):
    return (
        db.query(ProviderScheduleModel)
        .filter(
            ProviderScheduleModel.provider_id == provider_id,
            ProviderScheduleModel.is_booked == False,
        )
        .all()
    )
