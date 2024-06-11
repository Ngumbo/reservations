import datetime
import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.db.session import Base


class Appointment(Base):
    __tablename__ = "appointment"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider_schedule_id = Column(
        UUID(as_uuid=True), ForeignKey("provider_schedule.id"), nullable=False
    )
    client_id = Column(UUID(as_uuid=True), ForeignKey("client.id"), nullable=False)
    is_confirmed = Column(Boolean, default=False, nullable=False)
    is_expired = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.UTC),
        onupdate=datetime.datetime.now(datetime.UTC),
    )
