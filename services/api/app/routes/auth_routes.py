from fastapi import APIRouter, HTTPException
import requests
from fastapi.responses import JSONResponse

USER_SERVICE_URL = "http://user_service:5001"
AUTH_SERVICE_URL = "http://auth_service:5003"

auth_routes = APIRouter()

@auth_routes.post("/registration")
async def registration(user_data: dict):
    try:
        # Перенаправляем запрос на Flask-приложение
        response = requests.post(f"{USER_SERVICE_URL}/users/create_user", json=user_data)
        if not response.status_code == 201:
            return {"error": response.json()}, response.status_code
        
        user_service_response = response
        
        user_data = {}
        user_data["user_id"] = response.json().get("user", {}).get("user_id")
        user_data["email"] = response.json().get("user", {}).get("email")
        
        tokens = {}
        
        response = requests.post(f"{AUTH_SERVICE_URL}/generate_token/access", json=user_data)
        if not response.status_code == 201:
            return {"error": response.json()}, response.status_code
        
        tokens["access"] = response.json().get("token")
        
        response = requests.post(f"{AUTH_SERVICE_URL}/generate_token/refresh", json=user_data)
        if not response.status_code == 201:
            return {"error": response.json()}, response.status_code
        
        tokens["refresh"] = response.json().get("token")
        
        token_data = {}
        token_data["user_id"] = user_data["user_id"]
        token_data["token"] = tokens["refresh"]
        
        response = requests.post(f"{AUTH_SERVICE_URL}/save_token", json=token_data)
        if not response.status_code == 201:
            return {"error": response.json()}, response.status_code
        
        return {"user": user_service_response.json(), "auth": response.json()}

    except requests.RequestException as e:
        return {"error": f"Error communicating with user service: {str(e)}"}, 500

# @auth_routes.post("/registration")
# async def registration(user_data: dict):
#     try:
#         response = requests.post(f"{USER_SERVICE_URL}/users/create_user", json=user_data)
        
#         user_data["email"] = response.json().get("email")
#         user_data["user_id"] = response.json().get("user_id")
        
#         tokens = {}
        
#         response = requests.post(f"{AUTH_SERVICE_URL}/generate_token/access", json=user_data)
#         tokens["access_token"] = response.json().get("token")
        
#         response = requests.post(f"{AUTH_SERVICE_URL}/generate_token/refresh", json=user_data)
#         tokens["refresh_token"] = response.json().get("token")
        
#         token_data = {}
        
#         token_data["user_id"] = user_data["user_id"]
#         token_data["token"] = tokens["refresh_token"]
        
#         response = requests.post(f"{AUTH_SERVICE_URL}/save_token", json=token_data)
#         return response, 200

#     except requests.RequestException as e:
#         return {"error": f"Error: {str(e)}"}, 500
    
# @auth_routes.post("/login")
# async def registration(user_data: dict):
#     try:

#         # response = requests.post(f"{USER_SERVICE_URL}/users/create_user", json=user_data)
#         # if response.status_code == 201:
#         #     return {"message": "User created successfully", "user": response.json()}
#         # else:
#         #     return {"error": response.json()}, response.status_code

#     except requests.RequestException as e:
#         return {"error": f"Error communicating with user service: {str(e)}"}, 500
    
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