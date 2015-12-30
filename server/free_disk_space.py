#!/usr/bin/env python

from flask import Flask
from flask.ext.responses import json_response
import psutil

app = Flask(__name__)

@app.route("/space")
def space():
    result = {"space": (100-psutil.disk_usage("/").percent)}
    return json_response(result, status_code=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
