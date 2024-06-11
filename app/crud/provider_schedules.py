from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime

from app.models.provider_schedule import ProviderSchedule as ProviderScheduleModel
from app.schemas.crud.provider_schedule import ProviderScheduleCreate


def crud_get_provider_schedule_by_id(db: Session, provider_schedule_id: UUID):
    return (
        db.query(ProviderScheduleModel)
        .filter(
            ProviderScheduleModel.id == provider_schedule_id,
        )
        .first()
    )


def update_provider_schedule_booking(
    db: Session, provider_schedule_id: UUID, is_booked: bool
):
    provider_schedule = crud_get_provider_schedule_by_id(
        db=db, provider_schedule_id=provider_schedule_id
    )

    if provider_schedule:
        setattr(provider_schedule, "is_booked", is_booked)

        db.add(provider_schedule)
        db.commit()
        db.refresh(provider_schedule)


def crud_provider_schedule_exists(
    db: Session, provider_id: UUID, start_time: datetime, end_time: datetime
):
    return (
        db.query(ProviderScheduleModel)
        .filter(
            ProviderScheduleModel.provider_id == provider_id,
            ProviderScheduleModel.start_time == start_time,
            ProviderScheduleModel.end_time == end_time,
        )
        .first()
    )


def crud_create_provider_schedule(
    db: Session, provider_schedule: ProviderScheduleCreate
):
    schedule_exists = crud_provider_schedule_exists(
        db=db,
        provider_id=provider_schedule.provider_id,
        start_time=provider_schedule.start_time,
        end_time=provider_schedule.end_time,
    )
    if not schedule_exists:
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
