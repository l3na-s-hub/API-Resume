from pydantic import BaseModel
from typing import Optional
from datetime import date

class WorkExperienceResponse(BaseModel):
    id: int
    resume_id: int
    company: str
    position: str
    start_date: date
    end_date: Optional[date]
    responsibilities: Optional[str]
    
    class Config:
        from_attributes = True
