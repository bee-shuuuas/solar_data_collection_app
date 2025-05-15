# models.py
from app import db
from datetime import datetime

class DataEntry(db.Model):
    __tablename__ = 'data_entries'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    dust_weight = db.Column(db.Float, nullable=False)
    pyranometer_voltage = db.Column(db.Float, nullable=False)
    v_clean = db.Column(db.Float, nullable=False)
    i_clean = db.Column(db.Float, nullable=False)
    v_dusty = db.Column(db.Float, nullable=False)
    i_dusty = db.Column(db.Float, nullable=False)
    clean_panel_temp = db.Column(db.Float, nullable=False)
    dusty_panel_temp = db.Column(db.Float, nullable=False)
    ambient_shading_temp = db.Column(db.Float, nullable=False)
    ambient_surrounding_temp = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String(255), nullable=True)
    interval_time = db.Column(db.String(20), nullable=True)
    entry_time = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"<DataEntry {self.id}>"
