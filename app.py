from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# API: Temple Info
@app.route('/info', methods=['GET'])
def temple_info():
    return jsonify({
        "name": "Your Temple Name",
        "history": "This temple has a rich history...",
        "pooja_timings": "6:00 AM - 8:00 PM",
        "upcoming_events": ["Festival 1", "Festival 2"]
    })

# API: Donations
@app.route('/donate', methods=['POST'])
def donate():
    data = request.json
    return jsonify({"message": f"Donation of {data['amount']} received for {data['purpose']}!"})

if __name__ == '__main__':
    app.run(debug=True)
