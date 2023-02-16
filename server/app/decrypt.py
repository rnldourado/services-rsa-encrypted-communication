from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def decrypt_message(cipher_text,key):
    private_key = load_pem_private_key(key, password=None, backend=default_backend)


    plaintext = private_key.decrypt(
        cipher_text,
        OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )

    )

    plaintext = plaintext.decode("utf-8")
    print(plaintext)

    return plaintext