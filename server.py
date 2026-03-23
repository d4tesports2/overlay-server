from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 🔥 Global data store
live_data = {
    "teams": [],
    "top_players": [],
    "finish": "",
    "show_top5": True
}

# ✅ Home
@app.route("/")
def home():
    return "Server running 🚀"

# ✅ GET (OBS use karega)
@app.route("/data")
def data():
    return jsonify(live_data)

# ✅ POST (software data bhejega)
@app.route("/update", methods=["POST"])
def update():
    global live_data
    try:
        live_data = request.json
        print("🔥 DATA RECEIVED:", live_data)
        return {"status": "ok"}
    except Exception as e:
        return {"error": str(e)}

# ✅ Run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
