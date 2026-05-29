from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from app.db.session import get_session
from app.controllers.auth_controller import AuthController
from app.schemas.auth_schema import UserRegister, UserResponse, Token, UserLogin
from app.core.dependencies import get_current_active_user
from app.models.user import User

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserRegister, session: Session = Depends(get_session)):
    """Регистрация нового пользователя"""
    return AuthController.register(user_data, session)

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    """Вход в систему (получение JWT токена)"""
    credentials = UserLogin(username=form_data.username, password=form_data.password)
    return AuthController.login(credentials, session)

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    """Получить информацию о текущем пользователе"""
    return current_user
