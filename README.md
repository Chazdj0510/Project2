# 📢 Emergency Communication System

---

## 🚀 **Project Goals**
   - Develop a user-friendly web-based application to send emergency alerts via SMS using Twilio.
   - Integrate HTML5's Geolocation API to capture and transmit the user's location for precise emergency reporting.
   - Ensure the system is efficient, accessible, and responsive to facilitate quick emergency communication during wildfires.

The **Emergency Communication System** is a web-based application that allows users to send emergency alerts via SMS using Twilio. Users can capture their geolocation using HTML5's Geolocation API to provide additional context about their emergency. This system is designed to be simple, intuitive, and efficient, enabling users to send alerts with just a few clicks.

---

## Significance and Novelty of the Project
**Background Information:**
Wildfires are unpredictable and can spread rapidly, leaving limited time for individuals to react. Effective communication during such crises is vital to ensuring safety. However, traditional systems often lack speed and precise location data.

**Significance:**
This project addresses the need for a lightweight, fast, and reliable communication tool that provides real-time location data, significantly enhancing emergency response efficiency.

**Novelty:**
Unlike many existing emergency communication systems, this application combines SMS alerts with geolocation capabilities, ensuring accurate contextual information is shared. Its simplicity and accessibility set it apart, as users can quickly send alerts without requiring specialized equipment or extensive technical knowledge.


---

## Installation and Usage
**Installation:**
1. Clone the repository:
   ```bash
   git clone https://github.com/Chazdj0510/Project2.git
2. Navigate to the project directory:
   ```bash
   cd Project 2
3. Install dependencies
   1. **Python 3.x.**
   2. **Flask**: A lightweight Python web framework
   3. **Twilio SDK**
      ```bash
      pip install flask twilio
   - Sign Up for Twilio
     - Log in to your Twilio dashboard.
     - Get your Account SID and Auth Token from the dashboard.
     - Set up a Twilio phone number to send alerts.
4. Test Your Server
   - Replace `'your_twilio_account_sid'`, `'your_twilio_auth_token'`, and `'your_twilio_phone_number'` with your Twilio credentials.
   - Run the server:
     ```bash
     python server.py
   - Send a test POST request using Postman, cURL, or requests.

  

The project leverages the following tools and libraries:

- **Frontend**: HTML5, CSS, JavaScript
- **Backend**: Flask (Python)
- **SMS Gateway**: Twilio
- **Geolocation**: HTML5 Geolocation API
- **Development Server**: Flask (local development)
---

## 🛠️ **Setup Instructions**

### Prerequisites
Before you can run the project locally, ensure you have:

1. Python 3.x installed  
2. A Twilio account with credentials
3. Twilio's credentials (`Account SID`, `Auth Token`, and a Twilio phone number)

---

### Installation Steps

1. Clone the repository:
   ```bash
   git clone <https://github.com/Chazdj0510/Project2>
   cd EmergencyCommunicationSystem
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Set Twilio credentials in the server: Replace placeholders with your Twilio `Account SID`, `Auth Token`, and Twilio phone number:
   ```python
   client = Client("YOUR_TWILIO_ACCOUNT_SID", "YOUR_TWILIO_AUTH_TOKEN")
4. Run the server:
   ```bash
   python server.py
5. Open the frontend: Navigate to http://127.0.0.1:5000 in your browser.
