from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Course(SQLModel, table=True):
    __tablename__ = "courses"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resumes.id")
    name: str = Field(max_length=200)
    organization: Optional[str] = Field(default=None, max_length=200)
    year: Optional[int] = None
    
    resume: "Resume" = Relationship(back_populates="courses")
