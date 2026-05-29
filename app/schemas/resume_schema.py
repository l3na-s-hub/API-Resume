from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

class WorkExperienceCreate(BaseModel):
    company: str
    position: str
    start_date: date
    end_date: Optional[date] = None
    responsibilities: Optional[str] = None

class EducationCreate(BaseModel):
    institution: str
    degree: str
    start_date: date
    end_date: Optional[date] = None

class CourseCreate(BaseModel):
    name: str
    organization: Optional[str] = None
    year: Optional[int] = None

class LanguageCreate(BaseModel):
    language: str
    level: str

class ComputerSkillCreate(BaseModel):
    skill: str
    level: str

class ResumeCreate(BaseModel):
    passport: str
    secondname: str
    firstname: str
    patronymic: Optional[str] = None
    photo: Optional[str] = None
    email: EmailStr
    phone: str
    city: str
    address: str
    gender: str
    birth_date: date
    education_level: str
    marital_status: str
    has_children: bool
    military_service: bool
    position: str
    category_id: Optional[int] = None
    driver_license: Optional[str] = None
    personal_qualities: Optional[str] = None
    work_experiences: Optional[List[WorkExperienceCreate]] = []
    educations: Optional[List[EducationCreate]] = []
    courses: Optional[List[CourseCreate]] = []
    languages: Optional[List[LanguageCreate]] = []
    computer_skills: Optional[List[ComputerSkillCreate]] = []

class ResumeUpdate(BaseModel):
    secondname: Optional[str] = None
    firstname: Optional[str] = None
    patronymic: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    position: Optional[str] = None
    status: Optional[bool] = None
    category_id: Optional[int] = None

class ResumeResponse(BaseModel):
    id: int
    passport: str
    secondname: str
    firstname: str
    patronymic: Optional[str]
    email: str
    phone: str
    position: str
    status: bool
    
    class Config:
        from_attributes = True

class ResumeDetailResponse(BaseModel):
    id: int
    passport: str
    secondname: str
    firstname: str
    patronymic: Optional[str]
    photo: Optional[str]
    email: str
    phone: str
    city: str
    address: str
    gender: str
    birth_date: date
    education_level: str
    marital_status: str
    has_children: bool
    military_service: bool
    position: str
    category_id: Optional[int]
    status: bool
    driver_license: Optional[str]
    personal_qualities: Optional[str]
    
    class Config:
        from_attributes = True
