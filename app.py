from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from my first API!", "status": "running"})

@app.route('/mpesa')
def mpesa():
    return jsonify({"service": "M-Pesa API", "author": "Yusuf"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
