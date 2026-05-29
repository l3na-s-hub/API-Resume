# АРМ для поиска вакансий - Шубенкина Е.В.

REST API для формирования и поиска резюме 

## Функционал
- Создание резюме с полной информацией
- Поиск по ФИО, должности, категории
- Изменение статуса (активно/неактивно)
- Экспорт в Word/Excel

## Создать виртуальное окружение
python -m venv venv

## Активировать виртуальное окружение
### MacOs, Linux
source venv/bin/activate 
### Windows
.\venv\Scripts\activate

## Установка
pip install -r requirements.txt

*(Примечание для macOS: библиотека `uvloop` автоматически установится и будет использоваться для оптимизации процессов, на Windows она будет проигнорирована согласно маркерам в `requirements.txt`).*

## Запуск
uvicorn app.main:app --reload

## API Docs
http://localhost:8000/docs

## Скрипты для работы с БД

### Очистка базы данных
python scripts/clear_db.py
python -m scripts.clear_db

### Заполнение базы данных
python scripts/seed_data.py

# Запуск Django

## Настройка файла конфигурации 
### Windows, MacOs, Linux
cp .env.example .env

##  В файле .env укажите параметры подключения к вашей базе данных PostgreSQL в переменной `DATABASE_URL`:

DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/YOUR_DB_NAME
SECRET_KEY=YOUR_SECRET_KEY_HERE

## Применение миграций базы данных
python manage.py makemigrations
python manage.py migrate 

*Если в вашей базе данных уже существуют таблицы от версии FastAPI, используйте флаг `--fake-initial`, чтобы избежать конфликтов дублирования:
python manage.py migrate --fake-initial

## Загрузка статики
python manage.py collectstatic --noinput

## Запуск локального сервера
python manage.py runserver 8500
После этого проект будет доступен в браузере по адресу: http://127.0.0.1:8500/

python manage.py runserver
python manage.py createsuperuser