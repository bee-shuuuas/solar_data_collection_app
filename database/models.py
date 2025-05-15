# database/models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

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

    # New fields added
    clean_panel_temp = db.Column(db.Float, nullable=True)
    dusty_panel_temp = db.Column(db.Float, nullable=True)
    ambient_shading_temp = db.Column(db.Float, nullable=True)
    ambient_surrounding_temp = db.Column(db.Float, nullable=True)
    comment = db.Column(db.String(255), nullable=True)
    interval_time = db.Column(db.String(10), nullable=True)
    entry_time = db.Column(db.String(10), nullable=True)

