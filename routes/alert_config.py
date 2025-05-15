# routes/alert_config.py

from flask import Blueprint, request, jsonify
from datetime import datetime
import json
import os

alert_config_bp = Blueprint('alert_config', __name__)

ALERT_FILE = "alert_status.json"

# Initialize the alert status file if not exists
def init_alert_file():
    if not os.path.exists(ALERT_FILE):
        alert_data = {
            "alert_active": False,
            "alert_time": "",
            "sound_type": "bell",
            "next_alert_time": "",
            "alert_history": []
        }
        with open(ALERT_FILE, 'w') as f:
            json.dump(alert_data, f)

# Load alert configuration
def load_alert_config():
    with open(ALERT_FILE, 'r') as f:
        return json.load(f)

# Save alert configuration
def save_alert_config(data):
    with open(ALERT_FILE, 'w') as f:
        json.dump(data, f)

# Initialize the alert file on start
init_alert_file()

# ===============================
# ROUTES
# ===============================

# 🚀 **1. Configure Alert**
@alert_config_bp.route('/api/alert-config', methods=['POST'])
def configure_alert():
    try:
        data = request.json
        alert_data = load_alert_config()
        
        alert_data["alert_active"] = data.get("alert_active", False)
        alert_data["alert_time"] = data.get("alert_time", "")
        alert_data["sound_type"] = data.get("sound_type", "bell")
        
        if alert_data["alert_active"]:
            alert_data["next_alert_time"] = str(datetime.now())

        save_alert_config(alert_data)
        
        return jsonify({"message": "Alert configured successfully", "data": alert_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🚀 **2. Get Alert Status**
@alert_config_bp.route('/api/alert-status', methods=['GET'])
def get_alert_status():
    try:
        alert_data = load_alert_config()
        return jsonify(alert_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🚀 **3. Stop Alert**
@alert_config_bp.route('/api/alert-stop', methods=['POST'])
def stop_alert():
    try:
        alert_data = load_alert_config()
        alert_data["alert_active"] = False
        alert_data["next_alert_time"] = ""
        save_alert_config(alert_data)
        return jsonify({"message": "Alert stopped successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
