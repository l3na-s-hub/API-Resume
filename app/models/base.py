from sqlmodel import SQLModel
from datetime import datetime

class TimestampMixin(SQLModel):
    """Миксин для автоматических timestamp полей"""
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
