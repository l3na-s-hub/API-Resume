from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class AuditLog(SQLModel, table=True):
    __tablename__ = "audit_logs"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    action: str = Field(max_length=50)  # CREATE, UPDATE, DELETE, LOGIN
    entity_type: str = Field(max_length=50)  # Resume, Category, User
    entity_id: Optional[int] = None
    changes: Optional[str] = Field(default=None, max_length=5000)
    ip_address: Optional[str] = Field(default=None, max_length=50)
    user_agent: Optional[str] = Field(default=None, max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
