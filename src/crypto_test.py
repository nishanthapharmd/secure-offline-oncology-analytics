from cryptography.fernet import Fernet

def crypto_test():
    # Generate a key (for now, temporary)
    key = Fernet.generate_key()
    cipher = Fernet(key)

    message = b"research_secret_test"

    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)

    print("Original:", message)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    crypto_test()
