from sqlmodel import Session
from app.db.database import get_engine

def get_session():
    with Session(get_engine()) as session:
        yield session
