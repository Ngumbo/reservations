import pytest
from app.domain.provider_schedules import create_schedule_intervals
from datetime import datetime


def test_create_schedule_intervals():
    start_time = datetime(2024, 6, 30, 8, 0)
    end_time = datetime(2024, 6, 30, 9, 0)
    intervals = create_schedule_intervals(start_time=start_time, end_time=end_time)

    assert len(intervals) == 4
