from typing import Optional, List
from sqlmodel import select, or_, and_
from app.models.resume import Resume
from datetime import datetime, date

class ResumeFilters:
    
    @staticmethod
    def build_search_query(
        fio: Optional[str] = None,
        position: Optional[str] = None,
        category_id: Optional[int] = None,
        city: Optional[str] = None,
        min_age: Optional[int] = None,
        max_age: Optional[int] = None,
        status: bool = True
    ):
        """Построение сложного запроса для поиска резюме"""
        query = select(Resume).where(Resume.status == status)
        
        if fio:
            query = query.where(
                or_(
                    Resume.secondname.ilike(f"%{fio}%"),
                    Resume.firstname.ilike(f"%{fio}%"),
                    Resume.patronymic.ilike(f"%{fio}%")
                )
            )
        
        if position:
            query = query.where(Resume.position.ilike(f"%{position}%"))
        
        if category_id:
            query = query.where(Resume.category_id == category_id)
        
        if city:
            query = query.where(Resume.city.ilike(f"%{city}%"))
        
        if min_age or max_age:
            today = date.today()
            
            if min_age:
                max_birth_date = date(today.year - min_age, today.month, today.day)
                query = query.where(Resume.birth_date <= max_birth_date)
            
            if max_age:
                min_birth_date = date(today.year - max_age, today.month, today.day)
                query = query.where(Resume.birth_date >= min_birth_date)
        
        return query
