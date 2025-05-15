# alert_worker.py

import time
import json
from datetime import datetime
import os
from playsound import playsound

ALERT_FILE = "alert_status.json"

# Initialize the alert status file if it doesn't exist
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

# Sound alert (you can replace this with actual sound later)

# def play_sound(alert_type):
#     if alert_type == "bell":
#         print("🔔 Ringing Bell Alert!")
#     elif alert_type == "alarm":
#         print("🚨 Alarm Sound Activated!")
#     else:
#         print("🔊 Notification Sound Activated!")

def play_sound(alert_type):
    if alert_type == "bell":
        print("🔔 Ringing Bell Alert!")
        playsound('bell.mp3')
    elif alert_type == "alarm":
        print("🚨 Alarm Sound Activated!")
        playsound('alarm.mp3')
    else:
        print("🔊 Notification Sound Activated!")
        playsound('notification.mp3')



# Initialize the alert file on start
init_alert_file()

# Background loop to check for alerts
print("🔄 Starting Alert Worker...")

while True:
    alert_data = load_alert_config()

    if alert_data["alert_active"]:
        current_time = datetime.now().strftime("%H:%M")
        print(f"🕒 Current Time: {current_time}")
        print(f"⏲️ Alert Time: {alert_data['alert_time']}")

        if current_time == alert_data["alert_time"]:
            print(f"🔔 Alert Triggered at {current_time}!")
            play_sound(alert_data["sound_type"])

            # Log history
            alert_data["alert_history"].append(f"Alert triggered at {current_time}")
            
            # Stop the alert until re-configured
            alert_data["alert_active"] = False
            save_alert_config(alert_data)
            print("✅ Alert completed and deactivated.")
        else:
            print("⏳ Waiting for the correct time...")

    # Sleep for 10 seconds before checking again
    time.sleep(10)
