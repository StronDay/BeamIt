from flask import jsonify
from app.utils.token_util import TokenUtil
import requests

USER_SERVICE_URL = "http://user_service:5001"

class AuthController():
    
    def registration(user_data: dict):        
        
        login = user_data["login"]
        email = user_data["email"]
        password = user_data["password"]
        
        # Проверка валидности входных данных
        if not login or not password or not email:
            return jsonify({"error": "Both 'login' and 'password' and 'email' are required"}), 400
        
        # Создание нового пользователя если он ещё не создан
        response = requests.post(f"{USER_SERVICE_URL}/users/create_user", json=user_data)
        if response.status_code != 200:
            return jsonify(response.json()), response.status_code
        
        user_id = response.json().get("user_id")
        payload = {
            "user_id": user_id,
            "login": login,
        }
        
        # Создание токенов
        token_utils = TokenUtil()
        
        access_token = token_utils.generateAccess(payload)
        refresh_token = token_utils.generateRefresh(payload)
        token_utils.saveToken(user_id, refresh_token)
        
        return jsonify({
            "messege": "registration was successful", 
            "user_id": response.json().get("user_id"),
            "access_token": access_token,
            "refresh_token": refresh_token
        }), 200
    
    def login(user_data: dict):
        
        login = user_data["login"]
        password = user_data["password"]
        
        # Проверка валидности входных данных
        if not login or not password:
            return jsonify({"error": "Both 'login' and 'password' are required"}), 400
        
        # Проверка существования пользователя
        response = requests.get(f"{USER_SERVICE_URL}/users/get_user/{login}")
        if response.status_code != 200:
            return jsonify(response.json()), response.status_code
        
        user_id = response.json().get("user_id")
        payload = {
            "user_id": user_id,
            "login": login,
        }
        
        # Проверка валидности пароля
        response = requests.get(f"{USER_SERVICE_URL}/users/verify_password", json=user_data)
        if response.status_code != 200:
            return jsonify(response.json()), response.status_code
        
        # Создание токенов
        token_utils = TokenUtil()
        
        access_token = token_utils.generateAccess(payload)
        refresh_token = token_utils.generateRefresh(payload)
        token_utils.saveToken(user_id, refresh_token)
        
        return jsonify({
            "messege": "the login was completed successfully", 
            "user_id": user_id,
            "access_token": access_token,
            "refresh_token": refresh_token
        }), 200
    
    def logout(user_data: dict):
        return jsonify({"messege": "hello from AuthController[logout]"}), 200