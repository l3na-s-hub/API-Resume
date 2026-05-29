import re
from typing import Optional
from fastapi import HTTPException

class Validators:
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Валидация номера телефона"""
        pattern = r'^(\+7|8)?[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
        if not re.match(pattern, phone):
            raise HTTPException(400, "Неверный формат телефона")
        return True
    
    @staticmethod
    def validate_passport(passport: str) -> bool:
        """Валидация паспорта"""
        pattern = r'^\d{4}\s?\d{6}$'
        if not re.match(pattern, passport):
            raise HTTPException(400, "Неверный формат паспорта (например: 1234 567890)")
        return True
    
    @staticmethod
    def validate_age(birth_date: date) -> bool:
        """Проверка возраста (от 14 до 100 лет)"""
        from datetime import date
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        if age < 14 or age > 100:
            raise HTTPException(400, f"Возраст должен быть от 14 до 100 лет (текущий: {age})")
        return True
