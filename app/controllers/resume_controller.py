from fastapi import HTTPException, status
from sqlmodel import Session, select
from typing import List
from app.models.resume import Resume
from app.models.work_experience import WorkExperience
from app.models.education import Education
from app.models.course import Course
from app.models.language import Language
from app.models.computer_skill import ComputerSkill
from app.schemas.resume_schema import ResumeCreate, ResumeUpdate, ResumeResponse, ResumeDetailResponse

class ResumeController:
    @staticmethod
    def create_resume(data: ResumeCreate, session: Session) -> Resume:
        try:
            # Создаем резюме
            resume_dict = data.dict(exclude={'work_experiences', 'educations', 'courses', 'languages', 'computer_skills'})
            db_resume = Resume(**resume_dict)
            session.add(db_resume)
            session.commit()
            session.refresh(db_resume)
            
            # Добавляем опыт работы
            for exp in data.work_experiences:
                work_exp = WorkExperience(**exp.dict(), resume_id=db_resume.id)
                session.add(work_exp)
            
            # Добавляем образование
            for edu in data.educations:
                education = Education(**edu.dict(), resume_id=db_resume.id)
                session.add(education)
            
            # Добавляем курсы
            for crs in data.courses:
                course = Course(**crs.dict(), resume_id=db_resume.id)
                session.add(course)
            
            # Добавляем языки
            for lang in data.languages:
                language = Language(**lang.dict(), resume_id=db_resume.id)
                session.add(language)
            
            # Добавляем навыки
            for skill in data.computer_skills:
                comp_skill = ComputerSkill(**skill.dict(), resume_id=db_resume.id)
                session.add(comp_skill)
            
            session.commit()
            session.refresh(db_resume)
            return db_resume
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=str(e))
    
    @staticmethod
    def get_resume(resume_id: int, session: Session) -> Resume:
        resume = session.get(Resume, resume_id)
        if not resume:
            raise HTTPException(status_code=404, detail="Резюме не найдено")
        return resume
    
    @staticmethod
    def get_all_resumes(session: Session) -> List[Resume]:
        return session.exec(select(Resume)).all()
    
    @staticmethod
    def update_resume(resume_id: int, data: ResumeUpdate, session: Session) -> Resume:
        resume = session.get(Resume, resume_id)
        if not resume:
            raise HTTPException(status_code=404, detail="Резюме не найдено")
        
        update_data = data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(resume, key, value)
        
        session.add(resume)
        session.commit()
        session.refresh(resume)
        return resume
    
    @staticmethod
    def delete_resume(resume_id: int, session: Session):
        resume = session.get(Resume, resume_id)
        if not resume:
            raise HTTPException(status_code=404, detail="Резюме не найдено")
        session.delete(resume)
        session.commit()
        return {"message": "Резюме удалено"}
    
    @staticmethod
    def change_status(resume_id: int, status: bool, session: Session) -> Resume:
        resume = session.get(Resume, resume_id)
        if not resume:
            raise HTTPException(status_code=404, detail="Резюме не найдено")
        resume.status = status
        session.add(resume)
        session.commit()
        session.refresh(resume)
        return resume
