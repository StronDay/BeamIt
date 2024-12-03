from flask import Blueprint, request, jsonify, current_app
# from ..utils import Token

token_route = Blueprint("token_route", __name__)
# token_util = Token()

# @token_route.route("/generate_token/refresh", methods=['POST'])
# def generate_refresh():
#     try:
#         payload = request.get_json()
#         if not payload:
#             return jsonify({"error": "Invalid JSON"}), 400
        
#         token = token_util.generateRefresh(payload)
#         return jsonify({"token": token})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @token_route.route("/generate_token/access", methods=['POST'])
# def generate_access():
#     try:
#         payload = request.get_json()
#         if not payload:
#             return jsonify({"error": "Invalid JSON"}), 400
        
#         token = token_util.generateAccess(payload)
#         return jsonify({"token": token})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
# @token_route.route("/save_token", methods=['POST'])
# def save():
#     try:
#         data = request.get_json()
        
#         token = data.get("token")
#         user_id = data.get("user_id")

#         if not token or not user_id:
#             return jsonify({"error": "Both 'token' and 'user_id' are required"}), 400

#         result = token_util.saveToken(user_id, token)

#         if result is True:
#             return jsonify({"message": "Token saved successfully"}), 200
#         else:
#             return jsonify(result[0]), result[1]

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500  # Обработка ошибок на уровне маршрута