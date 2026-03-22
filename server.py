from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/live")
def live():
    with open("live.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

app.run(host="0.0.0.0", port=10000)