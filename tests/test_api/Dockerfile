FROM python:3

WORKDIR /test_api

RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "create_users.py"]