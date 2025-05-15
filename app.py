# app.py
from flask import Flask
from flask_cors import CORS
from routes.data_entry import data_entry_bp

# Initialize Flask App
app = Flask(__name__)

# Enable CORS to allow cross-origin requests from React Native
CORS(app)

# Register the Blueprint for API routes
app.register_blueprint(data_entry_bp)

# Root Route for Testing
@app.route('/')
def index():
    return "🚀 Solar Data Collection App Running Successfully with Supabase!"

# Start the Flask App
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
