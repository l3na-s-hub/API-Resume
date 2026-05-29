from typing import List
from fastapi import HTTPException
from sqlmodel import Session
from app.models.resume import Resume
from app.services.export_service import ExportService
from app.services.pdf_service import PDFService
from app.schemas.export_schema import ExportRequest, ExportResponse, ExportFormat
import os

class ExportController:
    
    @staticmethod
    def export_resumes(request: ExportRequest, session: Session) -> ExportResponse:
        resumes = []
        for resume_id in request.resume_ids:
            resume = session.get(Resume, resume_id)
            if resume:
                resumes.append(resume)
        
        if not resumes:
            raise HTTPException(status_code=404, detail="Резюме не найдены")
        
        if request.format == ExportFormat.WORD:
            if len(resumes) == 1:
                filename = ExportService.export_resume_to_word(resumes[0])
            else:
                raise HTTPException(400, "Word поддерживает только одно резюме")
        
        elif request.format == ExportFormat.EXCEL:
            filename = ExportService.export_resumes_to_excel(resumes)
        
        elif request.format == ExportFormat.PDF:
            if len(resumes) == 1:
                filename = PDFService.create_resume_pdf(resumes[0])
            else:
                raise HTTPException(400, "PDF поддерживает только одно резюме")
        
        else:
            raise HTTPException(400, "Неподдерживаемый формат")
        
        file_size = os.path.getsize(filename)
        
        return ExportResponse(
            filename=os.path.basename(filename),
            download_url=f"/api/v1/export/downloads/{os.path.basename(filename)}",  # ИСПРАВЛЕНО
            format=request.format.value,
            size_bytes=file_size
        )
