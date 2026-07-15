from flask import Flask, render_template
import socket
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        environment=os.getenv("APP_ENV", "Development"),
        version=os.getenv("APP_VERSION", "v1.0.0"),
        build_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
