from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/')
def home():
    return "Temple API is running!"

@app.route('/info', methods=['GET'])
def temple_info():
    return jsonify({
        "name": "Sree Thiruvilayanadu Bhagavathy Temple",
        "history": "Thiruvilayanadu Bhagavathy Temple Ethanur is a Hindu temple dedicated to Goddess Bhagavathy, located in Ethanur village, Palakkad district of Kerala. The temple is famous for its annual Kummatti festival, which is celebrated on every year March Month. The temple also conducts a Maha Kumbabhishekam (a ritual of consecration) every 12 years. The temple also has a pond and a banyan tree.",
        "pooja_timings": "6:00 AM - 8:00 PM",
        "upcoming_events": ["Ethanur Kummaty 2025", "Festival 2"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
