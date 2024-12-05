from fastapi import APIRouter, Depends
import requests
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

USER_SERVICE_URL = "http://user_service:5001"

users_route = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@users_route.get("/api/", response_class=JSONResponse)
def home():
    return {"message": "API Page"}

@users_route.get("/api/user/{user_id}")
async def get_user(user_id: str, access_token: str = Depends(oauth2_scheme)):
    try:

        response = requests.get(f"{USER_SERVICE_URL}/users/get_user/{user_id}")
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.json()}, response.status_code

    except requests.RequestException as e:
        return {"error": f"Error communicating with user service: {str(e)}"}, 500
    
@users_route.get("/api/users")
async def get_users(access_token: str = Depends(oauth2_scheme)):
    try:

        response = requests.get(f"{USER_SERVICE_URL}/users/get_users")
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.json()}, response.status_code

    except requests.RequestException as e:
        return {"error": f"Error communicating with user service: {str(e)}"}, 500