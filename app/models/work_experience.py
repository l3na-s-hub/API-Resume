from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date

class WorkExperience(SQLModel, table=True):
    __tablename__ = "work_experiences"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resumes.id")
    company: str = Field(max_length=200)
    position: str = Field(max_length=100)
    start_date: date
    end_date: Optional[date] = None
    responsibilities: Optional[str] = Field(default=None, max_length=1000)
    
    resume: "Resume" = Relationship(back_populates="work_experiences")
