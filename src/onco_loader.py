import base64
from pathlib import Path
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import pandas as pd
from io import StringIO

DATA_DIR = Path("data")

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def load_encrypted_csv(password: str, enc_filename: str) -> pd.DataFrame:
    salt = b"file_crypto_salt"
    key = derive_key(password, salt)
    cipher = Fernet(key)

    encrypted_path = DATA_DIR / enc_filename
    decrypted_bytes = cipher.decrypt(encrypted_path.read_bytes())

    csv_stream = StringIO(decrypted_bytes.decode())
    df = pd.read_csv(csv_stream)

    return df

if __name__ == "__main__":
    password = "strong_test_password"

    df = load_encrypted_csv(password, "onco_sample.csv.enc")

    print("Oncology dataset loaded into memory:")
    print(df)
    print("\nData types:")
    print(df.dtypes)
