from flask import render_template, request, jsonify
from app import app
from app.database import get_user_data, add_user_data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_user_data', methods=['GET'])
def get_data():
    data = get_user_data()
    return jsonify(data)

@app.route('/add_user_data', methods=['POST'])
def add_data():
    name = request.json.get('name')
    email = request.json.get('email')
    add_user_data(name, email)
    return jsonify({"message": "User data added successfully!"})
