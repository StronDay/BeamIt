from flask import Blueprint, request
from app.controllers.auth_controller import AuthController

auth_route = Blueprint("auth_route", __name__)

@auth_route.route("/registration", methods=['POST'])
def registration():
    return AuthController.registration(request.get_json())

@auth_route.route("/login", methods=['POST'])
def login():
    return AuthController.login(request.get_json())

@auth_route.route("/logout/<refresh_token>", methods=['POST'])
def logout(refresh_token):
    return AuthController.logout(refresh_token)