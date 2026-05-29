from sqlmodel import Session
from datetime import timedelta
from app.services.auth_service import AuthService
from app.schemas.auth_schema import UserLogin, UserRegister, Token, UserResponse
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

class AuthController:
    
    @staticmethod
    def login(credentials: UserLogin, session: Session) -> Token:
        user = AuthService.authenticate_user(
            credentials.username,
            credentials.password,
            session
        )
        
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = AuthService.create_access_token(
            data={"sub": user.username},
            expires_delta=access_token_expires
        )
        
        return Token(access_token=access_token, token_type="bearer")
    
    @staticmethod
    def register(user_data: UserRegister, session: Session) -> UserResponse:
        user = AuthService.register_user(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password,
            full_name=user_data.full_name,
            session=session
        )
        return UserResponse.from_orm(user)
