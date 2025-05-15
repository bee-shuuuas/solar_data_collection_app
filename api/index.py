# api/index.py - This is the file Vercel will use as the entry point
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "success", "message": "🚀 Solar Data Collection API is running!"})

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"status": "success", "data": "API test endpoint working"})

# Vercel requires this for Python serverless functions
if __name__ == '__main__':
    app.run(debug=True)
