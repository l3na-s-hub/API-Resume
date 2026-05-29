from fastapi import HTTPException
from sqlmodel import Session, select
from typing import List
from app.models.category import Category
from app.schemas.category_schema import CategoryCreate, CategoryResponse

class CategoryController:
    @staticmethod
    def create_category(data: CategoryCreate, session: Session) -> Category:
        db_category = Category(**data.dict())
        session.add(db_category)
        session.commit()
        session.refresh(db_category)
        return db_category
    
    @staticmethod
    def get_all_categories(session: Session) -> List[Category]:
        return session.exec(select(Category)).all()
    
    @staticmethod
    def get_category(category_id: int, session: Session) -> Category:
        category = session.get(Category, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Категория не найдена")
        return category
