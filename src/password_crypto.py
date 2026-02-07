import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def password_crypto_test():
    password = "strong_test_password"
    salt = b"fixed_salt_for_testing"

    key = derive_key(password, salt)
    cipher = Fernet(key)

    message = b"research_data_sample"

    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    password_crypto_test()
