from sqlmodel import Session, select
from app.db.database import engine
from app.models.user import User
from app.models.category import Category
from app.models.resume import Resume
from app.models.education import Education
from app.models.work_experience import WorkExperience
from app.models.course import Course
from app.models.language import Language
from app.models.computer_skill import ComputerSkill
from datetime import date

def seed_database():
    """Заполнение БД тестовыми данными"""
    
    with Session(engine) as session:
        
        print("Создание пользователей...")
        
        # Пользователь 1
        user1 = session.exec(select(User).where(User.username == "shubenkina")).first()
        if not user1:
            user1 = User(
                username="shubenkina",
                email="shubenkina@example.com",
                full_name="Шубенкина Елена Владимировна",
                is_active=True
            )
            user1.hashed_password = "pass123"
            session.add(user1)
        
        # Пользователь 2
        user2 = session.exec(select(User).where(User.username == "admin")).first()
        if not user2:
            user2 = User(
                username="admin",
                email="admin@example.com",
                full_name="Администратор",
                is_active=True
            )
            user2.hashed_password = "admin123"
            session.add(user2)
        
        session.commit()
        print("Пользователи созданы")
        
        print("Создание категорий...")
        categories_data = [
            {"name": "IT и программирование", "description": "Разработка ПО, тестирование"},
            {"name": "Продажи", "description": "Менеджеры по продажам"},
            {"name": "Маркетинг", "description": "SMM, контент"},
            {"name": "Дизайн", "description": "Графический дизайн"},
            {"name": "Бухгалтерия", "description": "Финансы"}
        ]
        
        for cat_data in categories_data:
            existing = session.exec(select(Category).where(Category.name == cat_data["name"])).first()
            if not existing:
                session.add(Category(**cat_data))
        
        session.commit()
        print("Категории созданы")
        
        print("Создание резюме...")
        
        # Резюме 1: Иванов Иван
        resume1 = Resume(
            passport="4012 345678",
            secondname="Иванов",
            firstname="Иван",
            patronymic="Иванович",
            email="ivanov@test.com",
            phone="+79001234567",
            city="Екатеринбург",
            address="ул. Ленина, 10",
            gender="Мужской",
            birth_date=date(1990, 1, 1),
            education_level="высшее",
            marital_status="Холост",
            has_children=False,
            military_service=True,
            position="Python разработчик",
            category_id=1,
            driver_license="B",
            personal_qualities="Ответственный, коммуникабельный",
            is_active=True
        )
        
        # Резюме 2: Петрова Анна
        resume2 = Resume(
            passport="4013 567890",
            secondname="Петрова",
            firstname="Анна",
            patronymic="Сергеевна",
            email="petrova@test.com",
            phone="+79009876543",
            city="Москва",
            address="ул. Тверская, 5",
            gender="Женский",
            birth_date=date(1995, 5, 15),
            education_level="высшее",
            marital_status="Не замужем",
            has_children=False,
            military_service=False,
            position="QA Engineer",
            category_id=1,
            personal_qualities="Внимательная, педантичная",
            is_active=True
        )
        
        # Резюме 3: Смирнов Алексей
        resume3 = Resume(
            passport="4014 123456",
            secondname="Смирнов",
            firstname="Алексей",
            patronymic="Дмитриевич",
            email="smirnov@test.com",
            phone="+79005551234",
            city="Санкт-Петербург",
            address="Невский проспект, 100",
            gender="Мужской",
            birth_date=date(1988, 12, 10),
            education_level="высшее",
            marital_status="Женат",
            has_children=True,
            military_service=True,
            position="Менеджер по продажам",
            category_id=2,
            driver_license="B, C",
            personal_qualities="Коммуникабельный, целеустремленный",
            is_active=True
        )
        
        # Резюме 4: Минин Арсений
        resume4 = Resume(
            passport="4015 789012",
            secondname="Минин",
            firstname="Арсений",
            patronymic="Андреевич",
            email="minin@test.com",
            phone="+79007778899",
            city="Екатеринбург",
            address="ул. Малышева, 50",
            gender="Мужской",
            birth_date=date(1993, 8, 20),
            education_level="высшее",
            marital_status="Холост",
            has_children=False,
            military_service=True,
            position="Frontend разработчик",
            category_id=1,
            driver_license="B",
            personal_qualities="Креативный, внимательный к деталям, быстро обучаемый",
            is_active=True
        )
        
        session.add_all([resume1, resume2, resume3, resume4])
        session.commit()
        session.refresh(resume1)
        session.refresh(resume2)
        session.refresh(resume3)
        session.refresh(resume4)
        print("Резюме созданы")
        
        print("Добавление образования...")
        educations = [
            Education(
                resume_id=resume1.id,
                institution="УрФУ им. Ельцина",
                degree="Бакалавр программной инженерии",
                start_date=date(2008, 9, 1),
                end_date=date(2012, 6, 30)
            ),
            Education(
                resume_id=resume2.id,
                institution="МГУ им. Ломоносова",
                degree="Бакалавр прикладной математики",
                start_date=date(2013, 9, 1),
                end_date=date(2017, 6, 30)
            ),
            Education(
                resume_id=resume3.id,
                institution="СПбГУ",
                degree="Бакалавр экономики",
                start_date=date(2006, 9, 1),
                end_date=date(2010, 6, 30)
            ),
            Education(
                resume_id=resume4.id,
                institution="УрФУ им. Ельцина",
                degree="Бакалавр информационных технологий",
                start_date=date(2011, 9, 1),
                end_date=date(2015, 6, 30)
            )
        ]
        session.add_all(educations)
        session.commit()
        print("Образование добавлено")
        
        print("Добавление опыта работы...")
        experiences = [
            WorkExperience(
                resume_id=resume1.id,
                company="IT Solutions Ltd",
                position="Junior Python Developer",
                start_date=date(2020, 1, 15),
                end_date=date(2022, 12, 31),
                responsibilities="Разработка веб-приложений на Django"
            ),
            WorkExperience(
                resume_id=resume1.id,
                company="Tech Innovations",
                position="Middle Python Developer",
                start_date=date(2023, 1, 10),
                end_date=None,
                responsibilities="REST API на FastAPI, PostgreSQL"
            ),
            WorkExperience(
                resume_id=resume2.id,
                company="QA Team Pro",
                position="QA Engineer",
                start_date=date(2021, 3, 1),
                end_date=None,
                responsibilities="Автотесты на Python, Selenium"
            ),
            WorkExperience(
                resume_id=resume3.id,
                company="Sales Master",
                position="Sales Manager",
                start_date=date(2018, 6, 1),
                end_date=None,
                responsibilities="B2B продажи, переговоры"
            ),
            WorkExperience(
                resume_id=resume4.id,
                company="Web Studio Design",
                position="Junior Frontend Developer",
                start_date=date(2019, 5, 1),
                end_date=date(2021, 12, 31),
                responsibilities="Верстка сайтов, HTML, CSS, JavaScript"
            ),
            WorkExperience(
                resume_id=resume4.id,
                company="Digital Agency Pro",
                position="Middle Frontend Developer",
                start_date=date(2022, 1, 10),
                end_date=None,
                responsibilities="React, Vue.js, адаптивная верстка"
            )
        ]
        session.add_all(experiences)
        session.commit()
        print("Опыт работы добавлен")
        
        print("Добавление курсов...")
        courses = [
            Course(resume_id=resume1.id, name="Python Professional", organization="Stepik", year=2023),
            Course(resume_id=resume1.id, name="FastAPI Advanced", organization="Udemy", year=2024),
            Course(resume_id=resume2.id, name="Автоматизация тестирования", organization="Skillbox", year=2022),
            Course(resume_id=resume4.id, name="React продвинутый курс", organization="Udemy", year=2023),
            Course(resume_id=resume4.id, name="JavaScript: полный курс", organization="Stepik", year=2022)
        ]
        session.add_all(courses)
        session.commit()
        print("Курсы добавлены")
        
        print("Добавление языков...")
        languages = [
            Language(resume_id=resume1.id, language="Английский", level="B2"),
            Language(resume_id=resume1.id, language="Немецкий", level="A1"),
            Language(resume_id=resume2.id, language="Английский", level="C1"),
            Language(resume_id=resume3.id, language="Английский", level="B1"),
            Language(resume_id=resume4.id, language="Английский", level="B2")
        ]
        session.add_all(languages)
        session.commit()
        print("Языки добавлены")
        
        print("Добавление навыков...")
        skills = [
            ComputerSkill(resume_id=resume1.id, skill="Python", level="Продвинутый"),
            ComputerSkill(resume_id=resume1.id, skill="FastAPI", level="Средний"),
            ComputerSkill(resume_id=resume1.id, skill="PostgreSQL", level="Средний"),
            ComputerSkill(resume_id=resume1.id, skill="Git", level="Продвинутый"),
            ComputerSkill(resume_id=resume2.id, skill="Python", level="Средний"),
            ComputerSkill(resume_id=resume2.id, skill="Selenium", level="Продвинутый"),
            ComputerSkill(resume_id=resume2.id, skill="Postman", level="Продвинутый"),
            ComputerSkill(resume_id=resume3.id, skill="MS Office", level="Продвинутый"),
            ComputerSkill(resume_id=resume3.id, skill="CRM", level="Средний"),
            ComputerSkill(resume_id=resume4.id, skill="JavaScript", level="Продвинутый"),
            ComputerSkill(resume_id=resume4.id, skill="React", level="Продвинутый"),
            ComputerSkill(resume_id=resume4.id, skill="Vue.js", level="Средний"),
            ComputerSkill(resume_id=resume4.id, skill="HTML/CSS", level="Продвинутый"),
            ComputerSkill(resume_id=resume4.id, skill="Git", level="Средний")
        ]
        session.add_all(skills)
        session.commit()
        print("Навыки добавлены")
        
        print("\nБАЗА ДАННЫХ ЗАПОЛНЕНА!")
        print("Создано: 2 пользователя, 5 категорий, 4 резюме")
        print("Резюме:")
        print("  - Иванов Иван - Python разработчик")
        print("  - Петрова Анна - QA Engineer")
        print("  - Смирнов Алексей - Менеджер по продажам")
        print("  - Минин Арсений - Frontend разработчик")

if __name__ == "__main__":
    seed_database()
