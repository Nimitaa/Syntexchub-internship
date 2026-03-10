from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64

KEY = b'12345678901234567890123456789012'  # 32-byte pre-shared key

def encrypt_message(message):
    iv = os.urandom(16)  # safe IV
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(iv + ciphertext)

def decrypt_message(ciphertext):
    data = base64.b64decode(ciphertext)
    iv = data[:16]
    encrypted_msg = data[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    message = unpad(cipher.decrypt(encrypted_msg), AES.block_size)
    return message.decode()