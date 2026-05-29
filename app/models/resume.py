from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date

class Resume(SQLModel, table=True):
    __tablename__ = "resumes"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Общая информация
    passport: str = Field(max_length=20, index=True)
    secondname: str = Field(max_length=50, index=True)
    firstname: str = Field(max_length=50, index=True)
    patronymic: Optional[str] = Field(default=None, max_length=60)
    photo: Optional[str] = Field(default=None, max_length=255)  # путь к фото
    email: str = Field(max_length=100, index=True)
    phone: str = Field(max_length=20)
    city: str = Field(max_length=50)
    address: str = Field(max_length=200)
    gender: str = Field(max_length=10)  # Мужской/Женский
    birth_date: date
    
    # Образование и статус
    education_level: str = Field(max_length=50)  # высшее/среднее
    marital_status: str = Field(max_length=50)
    has_children: bool = Field(default=False)
    military_service: bool = Field(default=False)
    
    # Должность и категория
    position: str = Field(max_length=100, index=True)
    category_id: Optional[int] = Field(default=None, foreign_key="categories.id")
    
    # Статус резюме
    status: bool = Field(default=True)  # активно/не активно
    
    # Дополнительная информация
    driver_license: Optional[str] = Field(default=None, max_length=100)
    personal_qualities: Optional[str] = Field(default=None, max_length=500)
    
    # Связи
    work_experiences: List["WorkExperience"] = Relationship(back_populates="resume")
    educations: List["Education"] = Relationship(back_populates="resume")
    courses: List["Course"] = Relationship(back_populates="resume")
    languages: List["Language"] = Relationship(back_populates="resume")
    computer_skills: List["ComputerSkill"] = Relationship(back_populates="resume")
    category: Optional["Category"] = Relationship(back_populates="resumes")
