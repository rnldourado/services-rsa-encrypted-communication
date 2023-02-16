from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes, serialization


def encrypt_message(message):

    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    public_key = key.public_key()

    message = message.encode('utf-8')

    cipher_text = public_key.encrypt(
        message,
        OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    private_key = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    return cipher_text, private_key
