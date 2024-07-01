from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate a key
def generate_key():
    return os.urandom(32)

# Encrypt an image
def encrypt_image(image_path, key):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(image_data) + encryptor.finalize()
    
    encrypted_image_path = image_path + '.enc'
    with open(encrypted_image_path, 'wb') as f:
        f.write(iv + encrypted_data)
    
    return encrypted_image_path

# Example usage
key = generate_key()
image_path = "path_to_image.png"
encrypted_image_path = encrypt_image(image_path, key)
print(f"Encrypted image saved to {encrypted_image_path}")
