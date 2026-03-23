from flask import Flask, jsonify

app = Flask(__name__)

# 🔥 Dummy data (replace later with OCR)
live_data = {
    "team1": ["Scout", "Mortal", "Jonathan"],
    "team2": ["Clutchgod", "Goblin"]
}

@app.route("/")
def home():
    return "Server running v2 🚀"

# ✅ IMPORTANT ROUTE (missing in your case)
@app.route("/data")
def get_data():
    return jsonify(live_data)

# (optional) update data from external app
@app.route("/update", methods=["POST"])
def update_data():
    global live_data
    from flask import request
    live_data = request.json
    return {"status": "updated"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
