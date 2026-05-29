from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class SearchFilters(BaseModel):
    """Расширенные фильтры для поиска резюме"""
    fio: Optional[str] = None
    position: Optional[str] = None
    category_id: Optional[int] = None
    city: Optional[str] = None
    education_level: Optional[str] = None
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    gender: Optional[str] = None
    has_driver_license: Optional[bool] = None
    military_service: Optional[bool] = None
    status: bool = True
    page: int = 1
    size: int = 10

class SearchResult(BaseModel):
    """Результат поиска с пагинацией"""
    total: int
    page: int
    size: int
    pages: int
    items: List[dict]

class AdvancedSearchRequest(BaseModel):
    """Продвинутый поиск"""
    keywords: Optional[List[str]] = None
    positions: Optional[List[str]] = None
    categories: Optional[List[int]] = None
    cities: Optional[List[str]] = None
    min_experience_years: Optional[int] = None
    languages: Optional[List[str]] = None
    skills: Optional[List[str]] = None
