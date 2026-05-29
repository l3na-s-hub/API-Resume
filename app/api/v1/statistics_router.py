from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.controllers.statistics_controller import StatisticsController
from typing import Dict, List

router = APIRouter()

@router.get("/general", response_model=Dict)
def get_general_statistics(session: Session = Depends(get_session)):
    """Общая статистика по резюме"""
    return StatisticsController.get_general_statistics(session)

@router.get("/by-category", response_model=List[Dict])
def get_category_statistics(session: Session = Depends(get_session)):
    """Статистика резюме по категориям"""
    return StatisticsController.get_category_statistics(session)

@router.get("/by-city", response_model=List[Dict])
def get_city_statistics(session: Session = Depends(get_session)):
    """Статистика резюме по городам"""
    return StatisticsController.get_city_statistics(session)
