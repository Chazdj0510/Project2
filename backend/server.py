from flask import Flask, request, jsonify
from twilio.rest import Client
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Twilio credentials
TWILIO_ACCOUNT_SID = 'your_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_auth_token_here'
TWILIO_PHONE_NUMBER = '+1234567890'

# Set up Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/')
def home():
    return jsonify({"message": "Emergency Communication System Active"}), 200


@app.route('/send_alert', methods=['POST'])
def send_alert():
    """
    Endpoint to send emergency alerts to users.
    Expects JSON data with keys: phone_number, message
    """
    try:
        # Log the incoming data
        data = request.json

        # Input Validation
        if not data or 'message' not in data:
            return jsonify({"error": "Invalid input: 'message' key is missing"}), 400

        phone_number = data['phone_number']
        message = data['message']
        user_location = data['location']

        # Send SMS
        message_instance = client.messages.create(
            body=f"{message} - Location: {user_location.get('latitude')}, {user_location.get('longitude')}",
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        return jsonify({"status": "Message sent", "sid": message_instance.sid}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
