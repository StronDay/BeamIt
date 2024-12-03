from flask import jsonify
import requests

from app.utils.token_util import TokenUtil

class TokenController():
    
    def refresh_token(refresh_token):
        
        token_util = TokenUtil
        token = token_util.inspectRefresh(refresh_token)
        token = "dsadas"
        
        return jsonify({"token": token}), 200