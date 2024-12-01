FROM python:3

WORKDIR /auth_service

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска Flask-приложения
CMD ["gunicorn", "--bind", "0.0.0.0:5003", "app.app:create_app()"]