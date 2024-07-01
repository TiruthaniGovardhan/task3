from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Decrypt an image
def decrypt_image(encrypted_image_path, key):
    with open(encrypted_image_path, 'rb') as f:
        encrypted_data = f.read()
    
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    decrypted_image_path = encrypted_image_path.replace('.enc', '_decrypted.png')
    with open(decrypted_image_path, 'wb') as f:
        f.write(decrypted_data)
    
    return decrypted_image_path

# Example usage
decrypted_image_path = decrypt_image(encrypted_image_path, key)
print(f"Decrypted image saved to {decrypted_image_path}")
