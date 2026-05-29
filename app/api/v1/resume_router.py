from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List
from app.db.session import get_session
from app.controllers.resume_controller import ResumeController
from app.schemas.resume_schema import ResumeCreate, ResumeUpdate, ResumeResponse, ResumeDetailResponse

router = APIRouter()

@router.post("/", response_model=ResumeDetailResponse, status_code=status.HTTP_201_CREATED)
def create_resume(resume_data: ResumeCreate, session: Session = Depends(get_session)):
    """Создать новое резюме"""
    return ResumeController.create_resume(resume_data, session)

@router.get("/", response_model=List[ResumeResponse])
def get_all_resumes(session: Session = Depends(get_session)):
    """Получить все резюме"""
    return ResumeController.get_all_resumes(session)

@router.get("/{resume_id}", response_model=ResumeDetailResponse)
def get_resume(resume_id: int, session: Session = Depends(get_session)):
    """Получить резюме по ID"""
    return ResumeController.get_resume(resume_id, session)

@router.put("/{resume_id}", response_model=ResumeDetailResponse)
def update_resume(resume_id: int, resume_data: ResumeUpdate, session: Session = Depends(get_session)):
    """Обновить резюме"""
    return ResumeController.update_resume(resume_id, resume_data, session)

@router.delete("/{resume_id}")
def delete_resume(resume_id: int, session: Session = Depends(get_session)):
    """Удалить резюме"""
    return ResumeController.delete_resume(resume_id, session)

@router.patch("/{resume_id}/status")
def change_resume_status(resume_id: int, status: bool, session: Session = Depends(get_session)):
    """Изменить статус резюме (активно/не активно)"""
    return ResumeController.change_status(resume_id, status, session)
