from fastapi import APIRouter, HTTPException, Cookie, Response, Request
from fastapi.responses import JSONResponse
import requests
import requests.cookies

AUTH_SERVICE_URL = "http://auth_service:5003"

auth_route = APIRouter()

@auth_route.post("/api/registration")
async def registration(user_data: dict, response: Response):
    
    auth_response = requests.post(f"{AUTH_SERVICE_URL}/registration", json=user_data)
    if auth_response.status_code != 200:
        raise HTTPException(status_code=auth_response.status_code, detail=auth_response.json())
    
    refresh_token = auth_response.json().get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=400, detail="refresh token not found in response")
    
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        max_age=7200
    )
    
    return auth_response.json()

@auth_route.post("/api/login")
async def login(user_data: dict, response: Response):
    
    auth_response = requests.post(f"{AUTH_SERVICE_URL}/login", json=user_data)
    if auth_response.status_code != 200:
        raise HTTPException(status_code=auth_response.status_code, detail=auth_response.json())
    
    refresh_token = auth_response.json().get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=404, detail="refresh token not found in response")
    
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        max_age=7200
    )
    
    return auth_response.json()

@auth_route.post("/api/logout")
async def logout(cookies_request: Request, coockies_response: Response):
    
    refresh_token = cookies_request.cookies.get("refresh_token")
    
    if not refresh_token:
        raise HTTPException(status_code=404, detail={"error": "token not found"})
    
    response = requests.post(f"{AUTH_SERVICE_URL}/logout/{refresh_token}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    
    coockies_response.delete_cookie("refresh_token")
    
    return response.json()

@auth_route.post("/api/refresh")
async def refresh(cookies_request: Request, coockies_response: Response):
    try:
        refresh_token = cookies_request.cookies.get("refresh_token")
        
        if not refresh_token:
            raise HTTPException(status_code=404, detail={"error": "token not found"})
        
        response = requests.post(f"{AUTH_SERVICE_URL}/refresh/{refresh_token}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        
        refresh_token = response.json().get("refresh_token")
        if not refresh_token:
            raise HTTPException(status_code=404, detail="refresh token not found in response")
        
        coockies_response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            max_age=7200
        )
        
        return response.json()
    except Exception as e:
                return {"error": str(e)}, 500