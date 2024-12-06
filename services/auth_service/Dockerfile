FROM python:3

WORKDIR /auth_service

RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    curl

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5003", "app.app:create_app()"]