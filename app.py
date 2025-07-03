from flask import Flask, request, jsonify
from firebase_config import db

app = Flask(__name__)

@app.route('/save_progress', methods=['POST'])
def save_progress():
    data = request.json
    user_id = data.get("user_id")
    progress_data = {
        "completed_lessons": data.get("completed_lessons"),
        "quiz_score": data.get("quiz_score"),
        "last_active": data.get("last_active")
    }
    db.collection("users").document(user_id).set(progress_data)
    return jsonify({"status": "success", "message": "Progress saved!"})

if __name__ == "__main__":
    app.run(debug=True)
