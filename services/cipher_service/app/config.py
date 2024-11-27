from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key")
    
    # Преобразование ENCRYPTION_KEY из hex-строки в байты с обработкой ошибок
    ENCRYPTION_KEY = os.urandom(32)
    # if encryption_key_str:
    #     try:
    #         ENCRYPTION_KEY = bytes.fromhex(encryption_key_str.strip())  # Преобразуем строку в байты
    #     except ValueError as e:
    #         raise ValueError("Invalid ENCRYPTION_KEY format. Ensure it is a valid hexadecimal string.") from e
    # else:
    #     ENCRYPTION_KEY = os.urandom(32)  # Генерация случайного ключа, если переменная окружения не задана