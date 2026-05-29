from pydantic import BaseModel
from typing import Optional
from datetime import date

class EducationResponse(BaseModel):
    id: int
    resume_id: int
    institution: str
    degree: str
    start_date: date
    end_date: Optional[date]
    
    class Config:
        from_attributes = True
