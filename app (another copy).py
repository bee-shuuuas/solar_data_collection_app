# app.py
from flask import Flask
from database import init_app
from database.models import db
import config

from routes.data_entry import data_entry_bp # Import the Blueprint 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS


# Initialize database
init_app(app)

# app.py
app.register_blueprint(data_entry_bp)  # Register Blueprints (This should be AFTER app is created)


# app.py
from routes.alert_config import alert_config_bp
app.register_blueprint(alert_config_bp)


@app.route('/')
def index():
    return "🚀 Solar Data Collection App Running Successfully!"

# app.py
from flask_cors import CORS

# Initialize CORS
CORS(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
