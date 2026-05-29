from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class ComputerSkill(SQLModel, table=True):
    __tablename__ = "computer_skills"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resumes.id")
    skill: str = Field(max_length=100)
    level: str = Field(max_length=50)  # начальный, средний, продвинутый
    
    resume: "Resume" = Relationship(back_populates="computer_skills")
