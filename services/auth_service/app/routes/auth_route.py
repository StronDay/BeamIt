from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import AuthController

auth_route = Blueprint("auth_route", __name__)

@auth_route.route("/registration", methods=['POST'])
def registration():
    return AuthController.registration(request.get_json())

@auth_route.route("/login", methods=['POST'])
def login():
    return AuthController.login(request.get_json())

@auth_route.route("/logout", methods=['POST'])
def logout():
    return AuthController.logout(request.get_json())