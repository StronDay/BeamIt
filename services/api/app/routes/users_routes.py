from fastapi import APIRouter
import requests
from fastapi.responses import JSONResponse

USER_SERVICE_URL = "http://user_service:5001"

users_routers = APIRouter()

@users_routers.get("/", response_class=JSONResponse)
def home():
    return {"message": "Home Page"}

@users_routers.get("/user/{user_id}")
async def get_user(user_id: str):
    try:

        response = requests.get(f"{USER_SERVICE_URL}/users/get_user/{user_id}")
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.json()}, response.status_code

    except requests.RequestException as e:
        return {"error": f"Error communicating with user service: {str(e)}"}, 500
    
@users_routers.get("/users")
async def get_users(user_id: str):
    try:

        response = requests.get(f"{USER_SERVICE_URL}/users/get_users")
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.json()}, response.status_code

    except requests.RequestException as e:
        return {"error": f"Error communicating with user service: {str(e)}"}, 500