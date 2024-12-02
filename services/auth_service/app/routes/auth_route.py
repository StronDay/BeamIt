from flask import Blueprint, request, jsonify, current_app
from ..utils import Token

import requests

USER_SERVICE_URL = "http://user_service:5001"

auth_route = Blueprint("auth_route", __name__)
token_util = Token()

@auth_route.route("/authenticate_user", methods=['GET'])
def authenticate_user():
    try:
        user_data = request.get_json()
        if not user_data:
            return jsonify({"error": "Missing JSON body"}), 400

        login = user_data.get("login")
        password = user_data.get("password")

        if not login or not password:
            return jsonify({"error": "Both 'login' and 'password' are required"}), 400

        # Проверить есть ли пользователь через внешний сервис
        response = requests.get(f"{USER_SERVICE_URL}/users/get_user/{login}")
        if response.status_code != 200:
            return jsonify({"error": response.json()}), response.status_code

        user_id = response.json().get("user_id")
        if not user_id:
            return jsonify({"error": "User ID not found in response"}), 500
        
        # Валидация пароля
        response = requests.get(f"{USER_SERVICE_URL}/users/verify_password", json=user_data)
        if response.status_code != 200:
            return jsonify({"error": response.json()}), response.status_code

        return jsonify({"verify": response.json().get("verify"), "user_id": user_id}), 200

    except requests.RequestException as e:
        return jsonify({"error": f"Error communicating with user service: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500