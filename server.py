from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Server running v2 🚀"

@app.route("/data")
def get_data():
    try:
        path = os.path.join(os.getcwd(), "live.json")
        with open(path, "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
