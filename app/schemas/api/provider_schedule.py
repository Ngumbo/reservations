from pydantic import BaseModel

from datetime import date
from app.schemas.crud.provider_schedule import ProviderSchedule


class ProviderScheduleCreate(BaseModel):
    schedule_date: date
    start_time_hour: int
    start_time_minute: int
    end_time_hour: int
    end_time_minute: int


class ProviderScheduleResponse(BaseModel):
    items: list[ProviderSchedule]
