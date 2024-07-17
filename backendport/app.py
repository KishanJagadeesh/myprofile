from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
CORS(app)

@app.route('/api/projects', methods=['GET'])
def get_projects():
    projects = [
        {"id": 1, "title": "Project 1", "description": "Description of project 1"},
        {"id": 2, "title": "Project 2", "description": "Description of project 2"},
    ]
    return jsonify(projects)

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
