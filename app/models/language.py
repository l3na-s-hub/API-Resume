from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Language(SQLModel, table=True):
    __tablename__ = "languages"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resumes.id")
    language: str = Field(max_length=50)
    level: str = Field(max_length=50)  # A1, A2, B1, B2, C1, C2
    
    resume: "Resume" = Relationship(back_populates="languages")
