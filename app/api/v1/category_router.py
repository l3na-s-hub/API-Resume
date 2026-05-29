from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List
from app.db.session import get_session
from app.controllers.category_controller import CategoryController
from app.schemas.category_schema import CategoryCreate, CategoryResponse

router = APIRouter()

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category_data: CategoryCreate, session: Session = Depends(get_session)):
    """Создать новую категорию (направление деятельности)"""
    return CategoryController.create_category(category_data, session)

@router.get("/", response_model=List[CategoryResponse])
def get_all_categories(session: Session = Depends(get_session)):
    """Получить все категории"""
    return CategoryController.get_all_categories(session)

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, session: Session = Depends(get_session)):
    """Получить категорию по ID"""
    return CategoryController.get_category(category_id, session)
