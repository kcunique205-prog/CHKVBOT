import base64
import os
import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives.asymmetric import rsa

# Helper functions

def b64tohex(b64_string):
    decoded = base64.b64decode(b64_string)
    return decoded.hex()

def hex_to_b64(hex_string):
    bytes_data = bytes.fromhex(hex_string)
    return base64.b64encode(bytes_data).decode()

# Class definitions

class SecureRandom:
    def next_bytes(self, size):
        return os.urandom(size)

class RSAKey:
    def __init__(self):
        self.public_key = None

    def set_public(self, public_key_n, public_key_e):
        n = int(public_key_n, 16)
        e = int(public_key_e, 16)
        self.public_key = rsa.RSAPublicNumbers(e, n).public_key(default_backend())

    def encrypt(self, text):
        if not self.public_key:
            raise ValueError("Public key not set")

        padded_text = self.pkcs1_pad(text)
        encrypted = self.public_key.encrypt(
            padded_text,
            padding.PKCS1v15()
        )
        return hex_to_b64(encrypted.hex())

    def pkcs1_pad(self, text, size=128):
        text_bytes = text.encode("utf-8")
        padding_size = size - len(text_bytes) - 3
        if padding_size < 8:
            raise ValueError("Message too long for RSA")
        padding = b"\x00" + os.urandom(padding_size)
        return b"\x00\x02" + padding + b"\x00" + text_bytes

# Encryption class

class ECrypt:
    PUBLIC_KEY_E = b64tohex("AQAB")

    def encrypt_value_api(self, val, key=None):
        if isinstance(val, int) and val < 10000:
            val = str(val)

        if not isinstance(val, str):
            raise ValueError("The value to be encrypted must be a string type.")

        key_to_use = b64tohex(key) if key else self.PUBLIC_KEY_N

        rsa_key = RSAKey()
        rsa_key.set_public(key_to_use, self.PUBLIC_KEY_E)
        return "eCrypted:" + rsa_key.encrypt(val)

# Example usage

# ecrypt_instance = ECrypt()
# # Replace `your_base64_key` with your actual base64-encoded key.
# result = ecrypt_instance.encrypt_value_api("4100390679388112", key="wMNkkSMDWy2peB7WsUA4JBFsVdiqWuFvEKeE5UvvNnSKOx5YvFnAvQyc/B5vATFNG2uxwfzgeLLiLRml+TjHOmR2uxNoGRdmocMnIKr93IxiAxHQcvLjVH2/+jQMwcX5cDOEFaLfv0rEyBt/nIisWrCIcjKrA9ilCPWK69Y3lpXJJ2b5eTScgPHwfIM8t9iFm/wE+89mz1Fd+y0AAR/9qovXQX8BVZvWBq6jy6SGt03bKQN+WhUbCQrVylI9C3IYBrQkvEutaRNKJz1ikfB082t7s2OZqFVLG6Vua55hu5fCTNl26Pz82HfoUwltNJCP6nUOcE9BwWZyReHFHVvsPQ==")
# print(result)
