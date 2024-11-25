from fastapi import APIRouter
import requests
from fastapi.responses import JSONResponse

USER_SERVICE_URL = "http://user_service:5001"

router = APIRouter()

@router.get("/", response_class=JSONResponse)
def home():
    return {"message": "Home Page"}

@router.post("/users/create_user")
async def create_user(user_data: dict):
    try:
        # Перенаправляем запрос на Flask-приложение
        response = requests.post(f"{USER_SERVICE_URL}/users/create_user", json=user_data)
        
        # Проверяем статус ответа от Flask
        if response.status_code == 201:
            return {"message": "User created successfully", "user": response.json()}
        else:
            return {"error": response.json()}, response.status_code

    except requests.RequestException as e:
        return {"error": f"Error communicating with user service: {str(e)}"}, 500

@router.get("/users/get_user/{user_id}")
async def get_user(user_id: str):
    try:
        # Перенаправляем запрос на Flask-приложение для получения пользователя
        response = requests.get(f"{USER_SERVICE_URL}/users/get_user/{user_id}")
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.json()}, response.status_code

    except requests.RequestException as e:
        return {"error": f"Error communicating with user service: {str(e)}"}, 500