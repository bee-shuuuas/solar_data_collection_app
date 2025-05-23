# database/__init__.py

from .models import db

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
