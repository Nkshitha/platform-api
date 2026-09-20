
from flask import Flask, jsonify
import os
import datetime
import platform

app = Flask(__name__)

APP_NAME = "platform-api"
APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
APP_ENV = os.environ.get("APP_ENV", "development")

@app.route('/')
def home():
    return jsonify({
        "service": APP_NAME,
        "version": APP_VERSION,
        "env": APP_ENV,
        "status": "running",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "host": platform.node()
    })

@app.route('/health')
def health():
    return jsonify({
        "healthy": True,
        "service": APP_NAME,
        "version": APP_VERSION,
        "timestamp": datetime.datetime.utcnow.isoformat()
    }), 200

@app.route('/metrics')
def metrics():
    return jsonify({
        "service": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV,
        "python": platform.python_version(),
        "uptime": "running"
    }), 200

@app.route('/ready')
def ready():
    return jsonify({"ready": True}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port, debug=False)
EOF
