from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# API: Temple Info
@app.route('/info', methods=['GET'])
def temple_info():
    return jsonify({
        "name": "Sree Thiruvilayanadu Bhagavathy Temple",
        "history": "Thiruvilayanadu Bhagavathy Temple Ethanur is a Hindu temple dedicated to Goddess Bhagavathy, located in Ethanur village, Palakkad district of Kerala. The temple is famous for its annual Kummatti festival, which is celebrated on every year March Month. The temple also conducts a Maha Kumbabhishekam (a ritual of consecration) every 12 years. The temple also has a pond and a banyan tree.",
        "pooja_timings": "6:00 AM - 8:00 PM",
        "upcoming_events": ["Ethanur Kummaty 2025", "Festival 2"]
    })

# API: Donations
@app.route('/donate', methods=['POST'])
def donate():
    data = request.json
    return jsonify({"message": f"Donation of {data['amount']} received for {data['purpose']}!"})

if __name__ == '__main__':
    app.run(debug=True)
