from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import init_db, close_db
from app.api.v1 import resume_router, category_router, search_router
from app.api.v1 import auth_router, export_router, statistics_router 

@asynccontextmanager
async def lifespan(app_instance: FastAPI):
    init_db()
    yield
    close_db()

app = FastAPI(
    title="АРМ для поиска вакансий - Шубенкина Е.В.",
    description="REST API для формирования резюме с аутентификацией и экспортом",
    version="2.0.0",
    lifespan=lifespan
)

app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["Аутентификация"])
app.include_router(resume_router.router, prefix="/api/v1/resumes", tags=["Резюме"])
app.include_router(category_router.router, prefix="/api/v1/categories", tags=["Категории"])
app.include_router(search_router.router, prefix="/api/v1/search", tags=["Поиск"])
app.include_router(export_router.router, prefix="/api/v1/export", tags=["Экспорт"])
app.include_router(statistics_router.router, prefix="/api/v1/statistics", tags=["Статистика"])

@app.get("/")
def root():
    return {"message": "АРМ Резюме API v2.0 - Шубенкина Е.В."}
