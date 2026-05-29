from sqlmodel import Session, select, func
from app.models.resume import Resume
from app.models.category import Category
from typing import Dict, List

class StatisticsController:
    
    @staticmethod
    def get_general_statistics(session: Session) -> Dict:
        """Общая статистика по резюме"""
        total_resumes = session.exec(select(func.count(Resume.id))).one()
        active_resumes = session.exec(
            select(func.count(Resume.id)).where(Resume.status == True)
        ).one()
        
        return {
            "total_resumes": total_resumes,
            "active_resumes": active_resumes,
            "inactive_resumes": total_resumes - active_resumes
        }
    
    @staticmethod
    def get_category_statistics(session: Session) -> List[Dict]:
        """Статистика по категориям"""
        stmt = (
            select(Category.name, func.count(Resume.id))
            .join(Resume, Resume.category_id == Category.id, isouter=True)
            .group_by(Category.name)
        )
        results = session.exec(stmt).all()
        
        return [
            {"category": name, "count": count}
            for name, count in results
        ]
    
    @staticmethod
    def get_city_statistics(session: Session) -> List[Dict]:
        """Статистика по городам"""
        stmt = (
            select(Resume.city, func.count(Resume.id))
            .where(Resume.status == True)
            .group_by(Resume.city)
            .order_by(func.count(Resume.id).desc())
        )
        results = session.exec(stmt).all()
        
        return [
            {"city": city, "count": count}
            for city, count in results
        ]
