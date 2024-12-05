from flask import Blueprint, jsonify
from app.controllers.token_controller import TokenController
from app.utils.token_util import TokenUtil

token_route = Blueprint("token_route", __name__)

@token_route.route("/refresh/<refresh_token>", methods=['POST'])
def refresh(refresh_token):
    return TokenController.refresh_token(refresh_token)


@token_route.route("/validate/access/<access_token>", methods=['GET'])
def validate_access(access_token):
    token = TokenUtil()
    return token.inspectAccess(access_token)

@token_route.route("/validate/refresh/<refresh_token>", methods=['GET'])
def validate_refresh(refresh):
    token = TokenUtil()
    return token.inspectRefresh(refresh)