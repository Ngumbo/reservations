from pydantic import BaseModel, ConfigDict
from datetime import datetime
from uuid import UUID


class BaseProviderSchedule(BaseModel):
    provider_id: UUID
    start_time: datetime
    end_time: datetime


class ProviderSchedule(BaseProviderSchedule):
    id: UUID

    model_config = ConfigDict(from_attributes=True)


class ProviderScheduleCreate(BaseProviderSchedule):
    is_booked: bool = False
