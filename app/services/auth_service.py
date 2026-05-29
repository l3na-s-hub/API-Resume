from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from sqlmodel import Session, select
from app.models.user import User
from fastapi import HTTPException
import os
from dotenv import load_dotenv
import hashlib

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

class AuthService:
    @staticmethod
    def get_password_hash(password: str) -> str:
        """Хеширование пароля с SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Проверка пароля"""
        return AuthService.get_password_hash(plain_password) == hashed_password
    
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def authenticate_user(username: str, password: str, session: Session) -> User:
        user = session.exec(select(User).where(User.username == username)).first()
        if not user:
            raise HTTPException(status_code=401, detail="Неверные учетные данные")
        if not AuthService.verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Неверные учетные данные")
        return user
    
    @staticmethod
    def register_user(username: str, email: str, password: str, full_name: Optional[str], session: Session) -> User:
        if len(password) < 6:
            raise HTTPException(status_code=400, detail="Пароль должен быть минимум 6 символов")
        
        existing_user = session.exec(select(User).where(User.username == username)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Пользователь уже существует")
        
        existing_email = session.exec(select(User).where(User.email == email)).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email уже используется")
        
        hashed_password = AuthService.get_password_hash(password)
        new_user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            full_name=full_name
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
