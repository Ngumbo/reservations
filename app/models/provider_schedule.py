import datetime
import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.db.session import Base


class ProviderSchedule(Base):
    __tablename__ = "provider_schedule"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider_id = Column(UUID(as_uuid=True), ForeignKey("provider.id"), nullable=False)
    is_booked = Column(Boolean, default=False, nullable=False)
    start_time = Column(DateTime, default=False, nullable=False)
    end_time = Column(DateTime, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
    )
