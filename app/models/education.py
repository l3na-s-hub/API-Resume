from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date

class Education(SQLModel, table=True):
    __tablename__ = "educations"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resumes.id")
    institution: str = Field(max_length=200)
    degree: str = Field(max_length=100)  # специальность
    start_date: date
    end_date: Optional[date] = None
    
    resume: "Resume" = Relationship(back_populates="educations")
