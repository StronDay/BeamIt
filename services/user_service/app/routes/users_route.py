from flask import Blueprint, request, jsonify
import requests
from sqlalchemy.exc import SQLAlchemyError

from ..models import UsersModel
from ..models import data_base

from ..utils import is_user_existing, encrypt_password, create_new_user

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
        }), 201

    except ConnectionError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@users_route.route("/users/get_user/<user_id>", methods=['GET'])
def get_user(user_id):
    try:

        user = UsersModel.query.filter_by(user_id=user_id).first()
        
        if not user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "user_id": user.user_id,
            "login": user.login,
            "email": user.email
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500