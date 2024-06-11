from uuid import UUID

from fastapi import APIRouter, Request, Depends

from app.db.session import get_db
from app.schemas.api.provider_schedule import (
    ProviderScheduleCreate,
    ProviderScheduleResponse,
)
from app.crud.provider_schedules import crud_get_provider_schedule
from app.domain.provider_schedules import create_schedule

from datetime import datetime, time

provider_schedules_router = r = APIRouter()


@r.post(
    "/provider_schedules/{provider_id}",
    response_model_exclude_none=True,
)
async def create_provider_schedule(
    request: Request,
    provider_id: UUID,
    provider_schedule: ProviderScheduleCreate,
    db=Depends(get_db),
):
    """
    Create provider schedule
    """

    start_time = datetime.combine(
        provider_schedule.schedule_date,
        time(provider_schedule.start_time_hour, provider_schedule.start_time_minute),
    )
    end_time = datetime.combine(
        provider_schedule.schedule_date,
        time(provider_schedule.end_time_hour, provider_schedule.end_time_minute),
    )
    create_schedule(
        db=db, provider_id=provider_id, start_time=start_time, end_time=end_time
    )


@r.get(
    "/provider_schedules/{provider_id}",
    response_model_exclude_none=True,
    response_model=ProviderScheduleResponse,
)
async def create_provider_schedule(
    request: Request,
    provider_id: UUID,
    db=Depends(get_db),
):
    schedule = crud_get_provider_schedule(db=db, provider_id=provider_id)

    return ProviderScheduleResponse(items=schedule)
