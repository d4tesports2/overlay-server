from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return "Server running ✅"

@app.route("/live")
def live():
    try:
        file_path = os.path.join(BASE_DIR, "live.json")
        with open(file_path, "r") as f:
            data = json.load(f)
        return jsonify(data)
    except:
        return jsonify({"error": "live.json not found"})
