import sys
import os

sys.path.insert(0, r"C:\Users\Elena\Desktop\API-Resume-main")

from sqlmodel import Session, text
from app.db.database import engine

def clear_database():
    with Session(engine) as session:
        session.execute(text("SET session_replication_role = 'replica'"))
        
        session.execute(text("DELETE FROM computer_skills"))
        session.execute(text("DELETE FROM languages"))
        session.execute(text("DELETE FROM courses"))
        session.execute(text("DELETE FROM work_experiences"))
        session.execute(text("DELETE FROM educations"))
        session.execute(text("DELETE FROM resumes"))
        session.execute(text("DELETE FROM categories"))
        
        session.execute(text("SET session_replication_role = 'origin'"))
        
        session.execute(text("ALTER SEQUENCE categories_id_seq RESTART WITH 1"))
        session.execute(text("ALTER SEQUENCE resumes_id_seq RESTART WITH 1"))
        session.execute(text("ALTER SEQUENCE work_experiences_id_seq RESTART WITH 1"))
        session.execute(text("ALTER SEQUENCE educations_id_seq RESTART WITH 1"))
        session.execute(text("ALTER SEQUENCE courses_id_seq RESTART WITH 1"))
        session.execute(text("ALTER SEQUENCE languages_id_seq RESTART WITH 1"))
        session.execute(text("ALTER SEQUENCE computer_skills_id_seq RESTART WITH 1"))
        
        session.commit()
        print("База данных очищена")

if __name__ == "__main__":
    clear_database()