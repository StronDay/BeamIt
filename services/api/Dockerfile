FROM python:3

WORKDIR /api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска Flask-приложения
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "5010"]