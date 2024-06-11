from pydantic import BaseModel, ConfigDict
from datetime import datetime
from uuid import UUID


class ProviderSchedule(BaseModel):
    provider_id: UUID
    start_time: datetime
    end_time: datetime

    model_config = ConfigDict(from_attributes=True)


class ProviderScheduleCreate(ProviderSchedule):
    is_booked: bool = False
