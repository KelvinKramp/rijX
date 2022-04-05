from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv
load_dotenv()


# DEFINE FUNCTIONS FOR ENCRYPTING FROM https://devqa.io/encrypt-decrypt-data-python/
def load_key():
    """
    Load the previously generated key
    """
    key = os.environ.get("ENCRYPTION_KEY")
    return key


def encrypt_message(message):
    """
    Encrypts a message
    """
    key = os.environ.get("ENCRYPTION_KEY")
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    return encrypted_message


def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    return decrypted_message.decode()


def decrypt(message):
    message = message.encode('utf-8')
    message = decrypt_message(message)
    return message


if __name__ == "__main__":
    pass