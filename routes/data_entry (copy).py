# routes/data_entry.py
from flask import Blueprint, request, jsonify
from database.models import DataEntry, db
from datetime import datetime
from database.supabase_client import insert_data, get_all_data

data_entry_bp = Blueprint('data_entry', __name__)

@data_entry_bp.route('/api/data-entry', methods=['POST'])
def add_data_entry():
    try:
        data = request.json
        new_entry = DataEntry(
            dust_weight=data.get('dust_weight', 0),
            pyranometer_voltage=data.get('pyranometer_voltage', 0),
            v_clean=data.get('v_clean', 0),
            i_clean=data.get('i_clean', 0),
            v_dusty=data.get('v_dusty', 0),
            i_dusty=data.get('i_dusty', 0),
            clean_panel_temp=data.get('clean_panel_temp', 0),
            dusty_panel_temp=data.get('dusty_panel_temp', 0),
            ambient_shading_temp=data.get('ambient_shading_temp', 0),
            ambient_surrounding_temp=data.get('ambient_surrounding_temp', 0),
            comment=data.get('comment', ""),
            interval_time=data.get('interval_time', ""),
            entry_time=data.get('entry_time', "")
        )
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({"message": "Data entry added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@data_entry_bp.route('/api/get-data', methods=['GET'])
def get_all_data():
    try:
        data_entries = DataEntry.query.all()
        results = []
        for entry in data_entries:
            results.append({
                "id": entry.id,
                "timestamp": entry.timestamp,
                "dust_weight": entry.dust_weight,
                "pyranometer_voltage": entry.pyranometer_voltage,
                "v_clean": entry.v_clean,
                "i_clean": entry.i_clean,
                "v_dusty": entry.v_dusty,
                "i_dusty": entry.i_dusty,
                "clean_panel_temp": entry.clean_panel_temp,
                "dusty_panel_temp": entry.dusty_panel_temp,
                "ambient_shading_temp": entry.ambient_shading_temp,
                "ambient_surrounding_temp": entry.ambient_surrounding_temp,
                "comment": entry.comment,
                "interval_time": entry.interval_time,
                "entry_time": entry.entry_time
            })
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
