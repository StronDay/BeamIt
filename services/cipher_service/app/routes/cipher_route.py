from flask import Blueprint, request, jsonify, current_app
from app.utils.cipher import CipherUtils

cipher_route = Blueprint("cipher", __name__)

@cipher_route.route("/encrypt", methods=["POST"])
def encrypt_message():
    data = request.json
    plaintext = data.get("message")
    if not plaintext:
        return jsonify({"error": "Message is required"}), 400

    # Создаём объект для шифрования
    cipher = CipherUtils(current_app.config["ENCRYPTION_KEY"])
    encrypted_message = cipher.encrypt(plaintext)
    return jsonify({"encrypted_message": encrypted_message.hex()}), 200

@cipher_route.route("/decrypt", methods=["POST"])
def decrypt_message():
    data = request.json
    ciphertext_hex = data.get("encrypted_message")
    if not ciphertext_hex:
        return jsonify({"error": "Encrypted message is required"}), 400

    # Дешифруем сообщение
    cipher = CipherUtils(current_app.config["ENCRYPTION_KEY"])
    try:
        ciphertext = bytes.fromhex(ciphertext_hex)
        decrypted_message = cipher.decrypt(ciphertext)
        return jsonify({"decrypted_message": decrypted_message}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400