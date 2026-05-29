from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class ExportFormat(str, Enum):
    WORD = "word"
    EXCEL = "excel"
    PDF = "pdf"

class ExportRequest(BaseModel):
    resume_ids: List[int]
    format: ExportFormat
    include_photo: bool = True
    template: Optional[str] = "default"

class ExportResponse(BaseModel):
    filename: str
    download_url: str
    format: str
    size_bytes: int
