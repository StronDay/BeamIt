from flask import jsonify
import requests

USER_SERVICE_URL = "http://user_service:5001"

from app.utils.token_util import TokenUtil

class TokenController():
    
    def refresh_token(refresh_token):
        try:
            if not refresh_token:
                return jsonify({"messege": "authorization error"}), 401
        
            token_util = TokenUtil()
            
            token = token_util.inspectRefresh(refresh_token)
            token_from_db = token_util.find_token(refresh_token)
            
            if not token or not token_from_db:
                return jsonify({"messege": "authorization error", "token": refresh_token}), 401
            
            login = token["login"]
            
            # Проверка существования пользователя
            response = requests.get(f"{USER_SERVICE_URL}/users/get_user/{login}")
            if response.status_code != 200:
                return jsonify(response.json()), response.status_code
            
            user_id = response.json().get("user_id")
            payload = {
                "user_id": user_id,
                "login": login,
            }
            
            access_token = token_util.generateAccess(payload)
            refresh_token = token_util.generateRefresh(payload)
            token_util.saveToken(user_id, refresh_token)
        
            return jsonify({
                "messege": "the refresh was completed successfully", 
                "user_id": user_id,
                "access_token": access_token,
                "refresh_token": refresh_token
            }), 200

        except Exception as e:
            return {"error": str(e)}, 500