from flask import Blueprint, request, jsonify
import requests
from sqlalchemy.exc import SQLAlchemyError

from ..models import UsersModel
from ..models import data_base

from ..utils import is_user_existing, encrypt_password, create_new_user, get_user_password

CIPHER_SERVICE_URL = "http://cipher_service:5002"

users_route = Blueprint('users_route', __name__) 

@users_route.route("/users/create_user", methods=["POST"])
def create_user():
    try:
        user_data = request.json
        login = user_data.get("login")
        passwd = user_data.get("password")
        email = user_data.get("email")

        if not login or not email or not passwd:
            return jsonify({"error": "Missing required fields"}), 400

        if is_user_existing(login, email):
            return jsonify({"error": "User with this login or email already exists"}), 400

        encrypted_passwd = encrypt_password(CIPHER_SERVICE_URL, passwd)
        new_user = create_new_user(data_base, login, encrypted_passwd, email)

        return jsonify({
            "message": "User created successfully",
            "user": {
                "user_id": new_user.user_id,
                "login": new_user.login,
                "email": new_user.email
            }
        }), 200

    except ConnectionError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# verify_password

@users_route.route("/users/verify_password", methods=['GET'])
def verify_password():
    try:
        user_data = request.get_json()
        if not user_data:
            return jsonify({"error": "Missing JSON body"}), 400

        login = user_data.get("login")
        password = user_data.get("password")

        if not login or not password:
            return jsonify({"error": "Both 'login' and 'password' are required"}), 400
        
        data_base_password = get_user_password(login)
        if not data_base_password:
            return data_base_password
        
        encrypted_passwd = encrypt_password(CIPHER_SERVICE_URL, password)
        
        if encrypted_passwd == data_base_password:
            return jsonify({"verify": "true"}), 200
        else:
            return jsonify({"verify": "false"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@users_route.route("/users/get_user/<login>", methods=['GET'])
def get_user(login):
    try:
        user = UsersModel.query.filter_by(login=login).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "user_id": user.user_id,
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@users_route.route("/users/get_users", methods=['GET'])
def get_users():
    try:
        
        users = UsersModel.query.all()
        users_list = [
            {
                "user_id": user.user_id,
                "login": user.login,
                "email": user.email
            }
            for user in users
        ]

        return jsonify({"users": users_list}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500