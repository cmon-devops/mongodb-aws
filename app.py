from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# Configuration for MongoDB
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://rishma45:Rishma45@mongodb.cfewwe6yo94m.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&retryWrites=falsee")  # Change this to your MongoDB URI
mongo = PyMongo(app)

@app.route('/')
def index():
    return "Welcome to the Flask-MongoDB App!"

@app.route('/data', methods=['POST'])
def add_data():
    data = request.json
    mongo.db.myCollection.insert_one(data)
    return jsonify({"message": "Data added successfully!"}), 201

@app.route('/data', methods=['GET'])
def get_data():
    data = mongo.db.myCollection.find()
    result = []
    for item in data:
        item['_id'] = str(item['_id'])  # Convert ObjectId to string
        result.append(item)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
