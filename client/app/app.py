import requests
from encrypt import encrypt_message
import json
import os


cipher_text, key = encrypt_message("Alô mundo")


data = {
    'message': cipher_text.hex(),
    'key': key.hex()
    }

json_data = json.dumps(data)

response = requests.post("http://192.168.0.2:5000/", json=json_data)
print(response.json(), response.status_code)
