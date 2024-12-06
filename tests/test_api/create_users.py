import sys
import random
import requests
from faker import Faker

API_URL = "http://api:5010"

def create_user():
    fake = Faker()

    user_data = {
        "login": fake.user_name(),
        "email": fake.email(),
        "password": fake.password()
    }
    
    response = requests.post(f"{API_URL}/api/registration", json=user_data)
    print(f"Created user {user_data['login']}: {response.json()}")

def main():
    for _ in range(10):  # Цикл на 15 пользователей
        create_user()
    sys.exit(0)

if __name__ == "__main__":
    main()