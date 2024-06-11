"""create appointment table

Revision ID: 506dfa1eaa72
Revises: ef5b0b5144ec
Create Date: 2024-06-11 13:40:56.400332

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = "506dfa1eaa72"
down_revision: Union[str, None] = "ef5b0b5144ec"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "appointment",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "provider_schedule_id",
            UUID(as_uuid=True),
            sa.ForeignKey("provider_schedule.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "client_id",
            UUID(as_uuid=True),
            sa.ForeignKey("client.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("is_confirmed", sa.Boolean, nullable=False),
        sa.Column("is_expired", sa.Boolean, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("appointment")
