FROM python:3

WORKDIR /cipher_service

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска Flask-приложения
CMD ["gunicorn", "--bind", "0.0.0.0:5002", "app.app:create_app()"]