import requests

def encrypt_password(cipher_service_url, password):
    """Шифрует пароль с помощью внешнего сервиса."""
    encrypt_message = {"message": password}
    try:
        response = requests.post(f"{cipher_service_url}/encrypt", json=encrypt_message)
        response.raise_for_status()  # Проверяем успешность запроса
        encrypted_passwd = response.json().get("encrypted_message")
        if not encrypted_passwd:
            raise ValueError("Encryption service returned empty response")
        return encrypted_passwd
    except requests.RequestException as e:
        raise ConnectionError(f"Error communicating with encryption service: {str(e)}")