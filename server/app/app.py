from flask import Flask, request, jsonify
from flask_cors import CORS
from decrypt import decrypt_message
import json


app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET', 'POST'])
def hello():
    data = request.get_json()
    data = json.loads(data)

    cipher_text = bytes.fromhex(data.get('message'))
    key = bytes.fromhex(data.get('key'))

    message = decrypt_message(cipher_text, key)

    response = {
        'message': message 
       
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run()
