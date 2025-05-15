# routes/data_entry.py
from flask import Blueprint, request, jsonify
from database.supabase_client import insert_data, get_all_data
from datetime import datetime
import traceback

data_entry_bp = Blueprint('data_entry', __name__)

@data_entry_bp.route('/api/data-entry', methods=['POST'])
def add_data_entry():
    try:
        data = request.json
        print("📱 Received data from mobile:", data)
        
        # 1️⃣ -- Remove `entry_time` from the data if present
        if 'entryTime' in data:
            data.pop('entryTime')
        
        # 2️⃣ -- Check `intervalTime` format and fix it if necessary
        interval_time = data.get('intervalTime', '') or ''
        if len(interval_time) == 5:  # If format is HH:MM, add ":00"
            interval_time = f"{interval_time}:00"
        
        # 3️⃣ -- Create a properly formatted entry with explicit type conversion
        new_entry = {
            "dust_weight": float(data.get('dustWeight', 0) or 0),
            "pyranometer_voltage": float(data.get('pyranometerVoltage', 0) or 0),
            "v_clean": float(data.get('vClean', 0) or 0),
            "i_clean": float(data.get('iClean', 0) or 0),
            "v_dusty": float(data.get('vDusty', 0) or 0),
            "i_dusty": float(data.get('iDusty', 0) or 0),
            "clean_panel_temp": float(data.get('cleanTemp', 0) or 0),
            "dusty_panel_temp": float(data.get('dustyTemp', 0) or 0),
            "ambient_shading_temp": float(data.get('shadingTemp', 0) or 0),
            "ambient_surrounding_temp": float(data.get('ambientTemp', 0) or 0),
            "comment": str(data.get('comment', "")),
            "interval_time": interval_time,
        }
        
        print("🔄 Transformed data for Supabase:", new_entry)
        response = insert_data(new_entry)

        if "error" not in response:
            return jsonify(response), 201
        else:
            print("❌ Error in Supabase Response:", response.get("error"))
            return jsonify(response), 400

    except Exception as e:
        print("❌ Exception occurred:")
        traceback.print_exc()  # This will print the error to your console
        return jsonify({"error": str(e)}), 500


@data_entry_bp.route('/api/get-data', methods=['GET'])
def get_all_entries():
    try:
        data = get_all_data()
        if "error" in data:
            return jsonify(data), 500
        else:
            return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# # routes/data_entry.py
# from flask import Blueprint, request, jsonify
# from database.supabase_client import insert_data, get_all_data
# from datetime import datetime
# import traceback

# data_entry_bp = Blueprint('data_entry', __name__)

# @data_entry_bp.route('/api/data-entry', methods=['POST'])
# def add_data_entry():
#     try:
#         data = request.json
        
#         # 1️⃣ -- Remove `entry_time` from the data
#         if 'entryTime' in data:
#             data.pop('entryTime')
        
#         # 2️⃣ -- Check `intervalTime` format and fix it if necessary
#         if 'intervalTime' in data:
#             if len(data['intervalTime']) == 5:  # If format is HH:MM, add ":00"
#                 data['intervalTime'] = f"{data['intervalTime']}:00"
        
#         new_entry = {
#             "dust_weight": data.get('dustWeight', 0),
#             "pyranometer_voltage": data.get('pyranometerVoltage', 0),
#             "v_clean": data.get('vClean', 0),
#             "i_clean": data.get('iClean', 0),
#             "v_dusty": data.get('vDusty', 0),
#             "i_dusty": data.get('iDusty', 0),
#             "clean_panel_temp": data.get('cleanTemp', 0),
#             "dusty_panel_temp": data.get('dustyTemp', 0),
#             "ambient_shading_temp": data.get('shadingTemp', 0),
#             "ambient_surrounding_temp": data.get('ambientTemp', 0),
#             "comment": data.get('comment', ""),
#             "interval_time": data.get('intervalTime', ""),
#         }
        
#         response = insert_data(new_entry)

#         if "error" not in response:
#             return jsonify(response), 201
#         else:
#             print("❌ Error in Supabase Response:", response["error"])
#             return jsonify(response), 400

#     except Exception as e:
#         print("❌ Exception occurred:")
#         traceback.print_exc()  # This will print the error to your console
#         return jsonify({"error": str(e)}), 500


# @data_entry_bp.route('/api/get-data', methods=['GET'])
# def get_all_entries():
#     try:
#         data = get_all_data()
#         if "error" in data:
#             return jsonify(data), 500
#         else:
#             return jsonify(data), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
