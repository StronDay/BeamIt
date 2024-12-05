from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
import requests

AUTH_SERVICE_URL = "http://auth_service:5003"

class JWTMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, included_routes: list[str]):
        super().__init__(app)
        self.included_routes = included_routes

    async def dispatch(self, request: Request, call_next):
        # Исключаем маршруты из проверки
        if request.url.path not in self.included_routes:
            return await call_next(request)

        # Извлекаем токен из заголовка Authorization
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            # raise HTTPException(status_code=401, detail="Unauthorized")
            return JSONResponse(content={"Unauthorized": "not token"}, status_code=401)

        token = auth_header.split(" ")[1]
        auth_response = requests.get(f"{AUTH_SERVICE_URL}/validate/access/{token}")
        # validate_token = auth_response.json().get("refresh_token")
        if not auth_response:
            # raise HTTPException(status_code=401, detail="Unauthorized")
            return JSONResponse(content={"Unauthorized": "invalid token"}, status_code=401)
        

        # Передаём запрос дальше
        return await call_next(request)