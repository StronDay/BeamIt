from flask import Blueprint, request, jsonify

from ..models import UsersModel
from ..models import data_base

users_route = Blueprint('users_route', __name__) 

# Метод для создания нового пользователя
@users_route.route("/users/create_user", methods=['POST'])
def create_user():
    try:
        # Получаем данные из тела запроса
        user_data = request.json
        user_id = user_data.get("id")
        login = user_data.get("login")
        passwd = user_data.get("password")
        email = user_data.get("email")

        # Проверка наличия всех необходимых данных
        if not user_id or not login or not email or not passwd:
            return jsonify({"error": "Missing required fields"}), 400

        # Проверяем, существует ли пользователь с таким ID в базе данных
        user = UsersModel.query.filter_by(user_id=user_id).first()
        if user:
            return jsonify({"error": "User already exists"}), 400

        # Создаем нового пользователя
        new_user = UsersModel(user_id=user_id, login=login, passwd=passwd, email=email)
        
        # Добавляем в базу данных
        data_base.session.add(new_user)
        data_base.session.commit()

        return jsonify({"message": "User created successfully", "user": {
            "user_id": new_user.user_id,
            "login": new_user.login,
            "email": new_user.email
        }}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Метод для получения пользователя по его user_id
@users_route.route("/users/get_user/<user_id>", methods=['GET'])
def get_user(user_id):
    try:
        # Ищем пользователя по user_id
        user = UsersModel.query.filter_by(user_id=user_id).first()
        
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Возвращаем данные о пользователе
        return jsonify({
            "user_id": user.user_id,
            "login": user.login,
            "email": user.email
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500