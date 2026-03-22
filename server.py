from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Base directory (important for Render)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def home():
    return "Server running ✅"


# TEST route (deployment check)
@app.route("/test123")
def test123():
    return "WORKING OK 🚀"


@app.route("/live")
def live():
    try:
        file_path = os.path.join(BASE_DIR, "live.json")

        if not os.path.exists(file_path):
            return jsonify({"error": "live.json file not found"})

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})


# Local run (Render ignore karega)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
