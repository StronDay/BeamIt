FROM python:3

WORKDIR /user_service

RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY wait-for-db.sh /usr/local/bin/wait-for-db.sh

# Делаем скрипт исполнимым
RUN chmod +x /usr/local/bin/wait-for-db.sh

# Указываем команду для запуска Flask-приложения с ожиданием базы данных
CMD ["/usr/local/bin/wait-for-db.sh", "postgres", "5432", "--", "gunicorn", "--bind", "0.0.0.0:5001", "app.app:create_app()"]


# Указываем команду для запуска Flask-приложения
# CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app.app:create_app()"]