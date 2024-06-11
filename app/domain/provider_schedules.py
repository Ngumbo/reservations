from datetime import datetime, timedelta
from uuid import UUID
from sqlalchemy.orm import Session
from app.schemas.crud.provider_schedule import ProviderScheduleCreate
from app.crud.provider_schedules import crud_create_provider_schedule


def create_schedule(
    db: Session, provider_id: UUID, start_time: datetime, end_time: datetime
):
    interval = timedelta(minutes=15)

    periods = []
    period_start = start_time
    while period_start < end_time:
        period_end = min(period_start + interval, end_time)
        periods.append((period_start, period_end))
        period_start = period_end

    print(periods)
    for period in periods:
        crud_create_provider_schedule(
            db=db,
            provider_schedule=ProviderScheduleCreate(
                provider_id=provider_id,
                start_time=period[0],
                end_time=period[1],
            ),
        )
