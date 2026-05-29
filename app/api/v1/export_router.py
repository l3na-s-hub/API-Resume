from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlmodel import Session
from app.db.session import get_session
from app.controllers.export_controller import ExportController
from app.schemas.export_schema import ExportRequest, ExportResponse
import os

router = APIRouter()

@router.post("/", response_model=ExportResponse)
def export_resumes(
    request: ExportRequest,
    session: Session = Depends(get_session)
):
    """Экспорт резюме в выбранном формате (Word/Excel/PDF)"""
    return ExportController.export_resumes(request, session)

@router.get("/downloads/{filename}")
def download_file(filename: str):
    """Скачать экспортированный файл"""
    # Проверяем все возможные папки
    for folder in ["word", "excel", "pdf"]:
        file_path = f"exports/{folder}/{filename}"
        if os.path.exists(file_path):
            return FileResponse(
                path=file_path,
                filename=filename,
                media_type='application/octet-stream'
            )
    
    raise HTTPException(status_code=404, detail=f"Файл {filename} не найден")
