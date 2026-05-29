from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select, or_
from typing import List
from app.db.session import get_session
from app.models.resume import Resume
from app.schemas.resume_schema import ResumeResponse

router = APIRouter()

@router.get("/by-fio", response_model=List[ResumeResponse])
def search_by_fio(fio: str = Query(..., description="ФИО для поиска"), session: Session = Depends(get_session)):
    """Поиск активных резюме по ФИО"""
    results = session.exec(
        select(Resume).where(
            or_(
                Resume.secondname.ilike(f"%{fio}%"),
                Resume.firstname.ilike(f"%{fio}%"),
                Resume.patronymic.ilike(f"%{fio}%")
            ),
            Resume.status == True
        )
    ).all()
    return results

@router.get("/by-position", response_model=List[ResumeResponse])
def search_by_position(position: str = Query(..., description="Должность"), session: Session = Depends(get_session)):
    """Поиск активных резюме по должности"""
    results = session.exec(
        select(Resume).where(
            Resume.position.ilike(f"%{position}%"),
            Resume.status == True
        )
    ).all()
    return results

@router.get("/by-position-and-category", response_model=List[ResumeResponse])
def search_by_position_and_category(
    position: str = Query(..., description="Должность"),
    category_id: int = Query(..., description="ID категории"),
    session: Session = Depends(get_session)
):
    """Поиск активных резюме по должности и направлению деятельности"""
    results = session.exec(
        select(Resume).where(
            Resume.position.ilike(f"%{position}%"),
            Resume.category_id == category_id,
            Resume.status == True
        )
    ).all()
    return results
