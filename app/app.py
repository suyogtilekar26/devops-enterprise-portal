from flask import Flask, render_template, jsonify
from datetime import datetime
import os
import time

app = Flask(__name__)

# Application start time
APP_START_TIME = time.time()

# Environment Variables
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "DEV")
BUILD_NUMBER = os.getenv("BUILD_NUMBER", "001")
DOCKER_IMAGE = os.getenv("DOCKER_IMAGE", "devops-enterprise-portal:v1")
GIT_COMMIT = os.getenv("GIT_COMMIT", "local-dev")


@app.route("/")
def home():

    uptime_seconds = int(time.time() - APP_START_TIME)

    hours = uptime_seconds // 3600
    minutes = (uptime_seconds % 3600) // 60
    seconds = uptime_seconds % 60

    uptime = f"{hours}h {minutes}m {seconds}s"

    return render_template(
        "index.html",
        version=APP_VERSION,
        environment=APP_ENV,
        build=BUILD_NUMBER,
        image=DOCKER_IMAGE,
        git_commit=GIT_COMMIT,
        deployment_time=datetime.now().strftime("%d-%b-%Y %H:%M:%S"),
        uptime=uptime,
    )


@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200


@app.route("/version")
def version():
    return jsonify({"version": APP_VERSION})


@app.route("/info")
def info():
    return jsonify({
        "environment": APP_ENV,
        "docker_image": DOCKER_IMAGE,
        "build": BUILD_NUMBER,
        "git_commit": GIT_COMMIT
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)