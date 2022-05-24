from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'msg': 'Hey, Street Stars!'})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    # deepcode ignore RunWithDebugTrue: <please specify a reason of ignoring this>
    app.run(debug=True, host='0.0.0.0', port=port)
