import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlmodel import Session
from app.db.database import engine
from app.models import (
    Category, Resume, WorkExperience, Education, 
    Course, Language, ComputerSkill
)
from datetime import date

def seed_database():
    with Session(engine) as session:
        # ========== КАТЕГОРИИ ==========
        categories = [
            Category(id=1, name="IT", description="Информационные технологии"),
            Category(id=2, name="Маркетинг", description="Маркетинг и реклама"),
            Category(id=3, name="Продажи", description="Продажи и работа с клиентами"),
            Category(id=4, name="Дизайн", description="Дизайн и визуальное искусство"),
            Category(id=5, name="Бухгалтерия", description="Бухгалтерский учет и финансы"),
        ]
        for cat in categories:
            session.add(cat)
        session.commit()
        print("Категории добавлены")

        # ========== РЕЗЮМЕ ==========
        resumes = [
            Resume(
                id=1, passport="4510 123456", secondname="Иванов", firstname="Иван", patronymic="Иванович",
                photo="photo1.jpg", email="ivanov@test.com", phone="+79001234567",
                city="Москва", address="ул. Ленина, 1", gender="Мужской", birth_date=date(1990, 1, 15),
                education_level="Высшее", marital_status="Женат", has_children=True, military_service=True,
                position="Python разработчик", category_id=1, status=True, driver_license="B",
                personal_qualities="Ответственный, целеустремленный"
            ),
            Resume(
                id=2, passport="4510 234567", secondname="Петрова", firstname="Елена", patronymic="Сергеевна",
                photo="photo2.jpg", email="petrova@test.com", phone="+79123456789",
                city="Санкт-Петербург", address="Невский пр., 10", gender="Женский", birth_date=date(1995, 5, 20),
                education_level="Высшее", marital_status="Замужем", has_children=False, military_service=False,
                position="Маркетолог", category_id=2, status=True, driver_license="B",
                personal_qualities="Креативная, коммуникабельная"
            ),
            Resume(
                id=3, passport="4510 345678", secondname="Сидоров", firstname="Алексей", patronymic="Владимирович",
                photo="photo3.jpg", email="sidorov@test.com", phone="+79234567890",
                city="Екатеринбург", address="ул. Малышева, 50", gender="Мужской", birth_date=date(1988, 11, 10),
                education_level="Среднее специальное", marital_status="Холост", has_children=False, military_service=True,
                position="Менеджер по продажам", category_id=3, status=True, driver_license="B,C",
                personal_qualities="Уверенный пользователь ПК, стрессоустойчивый"
            ),
            Resume(
                id=4, passport="4510 456789", secondname="Козлова", firstname="Мария", patronymic="Алексеевна",
                photo="photo4.jpg", email="kozlova@test.com", phone="+79345678901",
                city="Казань", address="ул. Баумана, 25", gender="Женский", birth_date=date(1992, 3, 25),
                education_level="Высшее", marital_status="Замужем", has_children=True, military_service=False,
                position="Графический дизайнер", category_id=4, status=False, driver_license="B",
                personal_qualities="Творческий подход, внимание к деталям"
            ),
            Resume(
                id=5, passport="4510 567890", secondname="Смирнов", firstname="Дмитрий", patronymic="Николаевич",
                photo="photo5.jpg", email="smirnov@test.com", phone="+79456789012",
                city="Новосибирск", address="Красный пр., 100", gender="Мужской", birth_date=date(1991, 7, 30),
                education_level="Высшее", marital_status="Женат", has_children=True, military_service=True,
                position="Бухгалтер", category_id=5, status=True, driver_license="B",
                personal_qualities="Внимательный, усидчивый"
            ),
        ]
        for resume in resumes:
            session.add(resume)
        session.commit()
        print("Резюме добавлены")

        # ========== ОПЫТ РАБОТЫ ==========
        work_experiences = [
            WorkExperience(id=1, resume_id=1, company="ООО ТехноСофт", position="Junior Python Developer", start_date=date(2020,1,1), end_date=date(2022,3,15), responsibilities="Разработка бэкенда на Django"),
            WorkExperience(id=2, resume_id=1, company="АО ИТ Решения", position="Python Developer", start_date=date(2022,4,1), end_date=None, responsibilities="Разработка REST API, оптимизация БД"),
            WorkExperience(id=3, resume_id=2, company="Рекламное агентство МедиаГрупп", position="Маркетолог-аналитик", start_date=date(2018,6,1), end_date=date(2021,12,31), responsibilities="Анализ рынка, настройка рекламы"),
            WorkExperience(id=4, resume_id=2, company="Digital-студия МедиаСтар", position="Senior маркетолог", start_date=date(2022,1,10), end_date=None, responsibilities="Управление командой, стратегическое планирование"),
            WorkExperience(id=5, resume_id=3, company="ООО Продажи Плюс", position="Менеджер по продажам", start_date=date(2019,9,1), end_date=date(2023,5,31), responsibilities="Поиск клиентов, заключение договоров"),
            WorkExperience(id=6, resume_id=3, company="ИП Сидоров А.В.", position="Руководитель отдела продаж", start_date=date(2023,6,1), end_date=None, responsibilities="Управление отделом, разработка стратегии"),
            WorkExperience(id=7, resume_id=4, company="Студия дизайна АртЛайн", position="Дизайнер-верстальщик", start_date=date(2021,2,1), end_date=date(2023,11,30), responsibilities="Создание макетов, верстка"),
            WorkExperience(id=8, resume_id=4, company="Агентство Креатив", position="Графический дизайнер", start_date=date(2023,12,1), end_date=None, responsibilities="Разработка брендбуков, иллюстрации"),
            WorkExperience(id=9, resume_id=5, company="ООО ФинансГрупп", position="Помощник бухгалтера", start_date=date(2020,8,1), end_date=date(2022,12,31), responsibilities="Первичная документация, отчетность"),
            WorkExperience(id=10, resume_id=5, company="ООО КонсалтингПрофи", position="Бухгалтер", start_date=date(2023,1,10), end_date=None, responsibilities="Ведение бухгалтерии, налоговые расчеты"),
        ]
        for exp in work_experiences:
            session.add(exp)
        session.commit()
        print("Опыт работы добавлен")

        # ========== ОБРАЗОВАНИЕ ==========
        educations = [
            Education(id=1, resume_id=1, institution="МГУ им. Ломоносова", degree="Магистр прикладной информатики", start_date=date(2015,9,1), end_date=date(2020,6,30)),
            Education(id=2, resume_id=2, institution="СПбГУ", degree="Магистр маркетинга", start_date=date(2014,9,1), end_date=date(2019,6,30)),
            Education(id=3, resume_id=3, institution="УрФУ", degree="Специалист по менеджменту", start_date=date(2013,9,1), end_date=date(2018,6,30)),
            Education(id=4, resume_id=4, institution="КФУ", degree="Бакалавр дизайна", start_date=date(2016,9,1), end_date=date(2020,6,30)),
            Education(id=5, resume_id=5, institution="НГУ", degree="Бакалавр экономики", start_date=date(2014,9,1), end_date=date(2018,6,30)),
        ]
        for edu in educations:
            session.add(edu)
        session.commit()
        print("Образование добавлено")
        # ========== КУРСЫ ==========
        courses = [
            Course(id=1, resume_id=1, name="Python Advanced", organization="Otus", year=2022),
            Course(id=2, resume_id=1, name="FastAPI Bootcamp", organization="Stepik", year=2023),
            Course(id=3, resume_id=2, name="Digital Marketing", organization="Skillbox", year=2021),
            Course(id=4, resume_id=2, name="Таргетированная реклама", organization="Нетология", year=2022),
            Course(id=5, resume_id=3, name="Управление продажами", organization="Деловая среда", year=2020),
            Course(id=6, resume_id=3, name="HR для руководителей", organization="Корпоративный университет", year=2021),
            Course(id=7, resume_id=4, name="Adobe Illustrator", organization="GeekBrains", year=2020),
            Course(id=8, resume_id=4, name="Figma PRO", organization="Яндекс.Практикум", year=2023),
            Course(id=9, resume_id=5, name="1С:Бухгалтерия", organization="1С-Учебный центр", year=2019),
            Course(id=10, resume_id=5, name="Налоговый учет", organization="Актион-Дистант", year=2022),
        ]
        for course in courses:
            session.add(course)
        session.commit()
        print("Курсы добавлены")

        # ========== ЯЗЫКИ ==========
        languages = [
            Language(id=1, resume_id=1, language="Английский", level="Upper-Intermediate"),
            Language(id=2, resume_id=1, language="Немецкий", level="Pre-Intermediate"),
            Language(id=3, resume_id=2, language="Английский", level="Advanced"),
            Language(id=4, resume_id=3, language="Английский", level="Intermediate"),
            Language(id=5, resume_id=4, language="Английский", level="Intermediate"),
            Language(id=6, resume_id=4, language="Французский", level="Elementary"),
            Language(id=7, resume_id=5, language="Английский", level="Pre-Intermediate"),
        ]
        for lang in languages:
            session.add(lang)
        session.commit()
        print("Языки добавлены")

        # ========== НАВЫКИ ==========
        skills = [
            ComputerSkill(id=1, resume_id=1, skill="Python", level="Advanced"),
            ComputerSkill(id=2, resume_id=1, skill="Django/FastAPI", level="Advanced"),
            ComputerSkill(id=3, resume_id=1, skill="PostgreSQL", level="Intermediate"),
            ComputerSkill(id=4, resume_id=1, skill="Docker", level="Intermediate"),
            ComputerSkill(id=5, resume_id=2, skill="Google Analytics", level="Expert"),
            ComputerSkill(id=6, resume_id=2, skill="Яндекс.Директ", level="Advanced"),
            ComputerSkill(id=7, resume_id=2, skill="Excel", level="Advanced"),
            ComputerSkill(id=8, resume_id=3, skill="1С:CRM", level="Advanced"),
            ComputerSkill(id=9, resume_id=3, skill="Salesforce", level="Intermediate"),
            ComputerSkill(id=10, resume_id=4, skill="Photoshop", level="Advanced"),
            ComputerSkill(id=11, resume_id=4, skill="Figma", level="Expert"),
            ComputerSkill(id=12, resume_id=4, skill="Illustrator", level="Advanced"),
            ComputerSkill(id=13, resume_id=5, skill="1С:Предприятие", level="Expert"),
            ComputerSkill(id=14, resume_id=5, skill="Excel", level="Advanced"),
            ComputerSkill(id=15, resume_id=5, skill="КонсультантПлюс", level="Advanced"),
        ]
        for skill in skills:
            session.add(skill)
        session.commit()
        print("Навыки добавлены")

        print("\nБаза данных успешно заполнена тестовыми данными!")

if __name__ == "__main__":
    seed_database()