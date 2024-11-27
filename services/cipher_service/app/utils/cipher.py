from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

class CipherUtils:
    def __init__(self, key: bytes):
        self.key = key

    def encrypt(self, plaintext: str) -> bytes:
        iv = os.urandom(16)  # Инициализационный вектор
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        # Выравнивание данных перед шифрованием
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()

        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return iv + encrypted_data  # Возвращаем IV + зашифрованный текст

    def decrypt(self, ciphertext: bytes) -> str:
        iv = ciphertext[:16]  # Извлекаем IV
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        encrypted_data = ciphertext[16:]
        decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Убираем выравнивание
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
        return decrypted_data.decode()