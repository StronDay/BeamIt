from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

import requests

USER_SERVICE_URL = "http://user_service:5001"
AUTH_SERVICE_URL = "http://auth_service:5003"

auth_routes = APIRouter()

@auth_routes.post("/registration")
async def registration(user_data: dict):
    try:
        # Отправка данных в user_service
        response = requests.post(f"{USER_SERVICE_URL}/users/create_user", json=user_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        
        user_service_response = response.json()
        
        # Формируем данные пользователя
        user_data = {
            "user_id": user_service_response.get("user", {}).get("user_id"),
            "email": user_service_response.get("user", {}).get("email"),
        }

        tokens = {}

        # Генерация access-токена
        response = requests.post(f"{AUTH_SERVICE_URL}/generate_token/access", json=user_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        tokens["access"] = response.json().get("token")

        # Генерация refresh-токена
        response = requests.post(f"{AUTH_SERVICE_URL}/generate_token/refresh", json=user_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        tokens["refresh"] = response.json().get("token")

        # Сохранение refresh-токена
        token_data = {
            "user_id": user_data["user_id"],
            "token": tokens["refresh"]
        }
        
        response = requests.post(f"{AUTH_SERVICE_URL}/save_token", json=token_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())

        # Создание ответа и установка cookie
        response = JSONResponse(
            content={"user": user_service_response, "message": "User registered successfully"}
        )
        
        response.set_cookie(key="refresh_token", value=tokens["refresh"], max_age=7200, httponly=True)
        return response

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with external service: {str(e)}")
    
@auth_routes.post("/login")
async def login(user_data: dict):
    try:
        
        response = requests.get(f"{AUTH_SERVICE_URL}/authenticate_user", json=user_data)
        if not response.status_code == 200:
            return {"error": response.json()}, response.status_code
        
        if response.json().get("verify") == "false":
            return {"message": "invalid password"}
        
        user_data["user_id"] = response.json().get("user_id")

        tokens = {}

        # Генерация access-токена
        response = requests.post(f"{AUTH_SERVICE_URL}/generate_token/access", json=user_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        tokens["access"] = response.json().get("token")

        # Генерация refresh-токена
        response = requests.post(f"{AUTH_SERVICE_URL}/generate_token/refresh", json=user_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        tokens["refresh"] = response.json().get("token")

        # Сохранение refresh-токена
        token_data = {
            "user_id": user_data["user_id"],
            "token": tokens["refresh"]
        }
        
        response = requests.post(f"{AUTH_SERVICE_URL}/save_token", json=token_data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())

        # Создание ответа и установка cookie
        response = JSONResponse(
            content={"message": "User login successfully"}
        )
        
        response.set_cookie(key="refresh_token", value=tokens["refresh"], max_age=7200, httponly=True)
        return response

    except requests.RequestException as e:
        return {"error": f"Error communicating with user service: {str(e)}"}, 500
    
# @auth_routers.post("/logout")
# async def registration(user_data: dict):
#     try:

#         # response = requests.post(f"{USER_SERVICE_URL}/users/create_user", json=user_data)
#         # if response.status_code == 201:
#         #     return {"message": "User created successfully", "user": response.json()}
#         # else:
#         #     return {"error": response.json()}, response.status_code

#     except requests.RequestException as e:
#         return {"error": f"Error communicating with user service: {str(e)}"}, 500
    
# @auth_routes.post("/refresh")
# async def registration(user_data: dict):
#     try:

#         # response = requests.post(f"{USER_SERVICE_URL}/users/create_user", json=user_data)
#         # if response.status_code == 201:
#         #     return {"message": "User created successfully", "user": response.json()}
#         # else:
#         #     return {"error": response.json()}, response.status_code

#     except requests.RequestException as e:
#         return {"error": f"Error communicating with user service: {str(e)}"}, 500