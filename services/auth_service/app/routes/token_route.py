from flask import Blueprint, jsonify
from app.controllers.token_controller import TokenController

token_route = Blueprint("token_route", __name__)

@token_route.route("/refresh/<refresh_token>", methods=['POST'])
def refresh(refresh_token):
    return TokenController.refresh_token(refresh_token)