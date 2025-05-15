# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Add this import
from flask_migrate import Migrate  # Add this import
from database import init_app
import config
from routes.data_entry import data_entry_bp

app = Flask(__name__)
app.config.from_object('config')

# Choose one approach:
# Option 1: Use existing db instance
from database.models import db  # Import db from models
migrate = Migrate(app, db)
db.init_app(app)  # Initialize the db with app

# Option 2 (alternative): Create new instances
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# Register blueprints
app.register_blueprint(data_entry_bp)

if __name__ == "__main__":
    app.run(debug=True)
