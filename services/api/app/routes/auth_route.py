from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import requests

AUTH_SERVICE_URL = "http://auth_service:5003"

auth_route = APIRouter()

@auth_route.post("/api/registration")
async def registration(user_data: dict):
    
    response = requests.post(f"{AUTH_SERVICE_URL}/registration", json=user_data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    refresh_token = response.json().get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=400, detail="refresh token not found in response")
    
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        max_age=7200
    )
    
    return response.json()

@auth_route.post("/api/login")
async def login(user_data: dict):
    
    response = requests.post(f"{AUTH_SERVICE_URL}/login", json=user_data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    refresh_token = response.json().get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=400, detail="refresh token not found in response")
    
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        max_age=7200
    )
    
    return response.json()

@auth_route.post("/api/logout")
async def logout(user_data: dict):
    
    response = requests.post(f"{AUTH_SERVICE_URL}/logout", json=user_data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    return response.json()