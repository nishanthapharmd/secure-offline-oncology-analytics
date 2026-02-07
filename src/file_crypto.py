import base64
from pathlib import Path
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

DATA_DIR = Path("data")

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(password: str, input_filename: str):
    salt = b"file_crypto_salt"
    key = derive_key(password, salt)
    cipher = Fernet(key)

    input_path = DATA_DIR / input_filename
    output_path = DATA_DIR / f"{input_filename}.enc"

    plaintext = input_path.read_bytes()
    encrypted = cipher.encrypt(plaintext)

    output_path.write_bytes(encrypted)

    print(f"Encrypted file created: {output_path.name}")

def decrypt_file(password: str, enc_filename: str):
    salt = b"file_crypto_salt"
    key = derive_key(password, salt)
    cipher = Fernet(key)

    encrypted_path = DATA_DIR / enc_filename
    decrypted = cipher.decrypt(encrypted_path.read_bytes())

    print("Decrypted preview (first 100 chars):")
    print(decrypted[:100].decode())

if __name__ == "__main__":
    password = "strong_test_password"

    encrypt_file(password, "onco_sample.csv")
    decrypt_file(password, "onco_sample.csv.enc")
