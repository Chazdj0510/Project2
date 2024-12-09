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
   cd Project2
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

### Usage
1. Open the application in a web browser.
2. Grant location permissions when prompted.
3. Enter the recipient’s phone number and optional additional details about the emergency.
4. Click Send Alert to transmit the SMS along with your geolocation.

## Code Structure
The project leverages the following tools and libraries:

- **Frontend**: HTML5, CSS, JavaScript
   - Handles user interactions and geolocation capture.
- **Backend**: Flask (Python), Twilio, Geolocation API
   - Processes SMS sending via Twilio and manages API endpoints.

| User Interface            |
| :--------------------:    |
|   ↓                        |
| Frontend (HTML/JavaScript) |
|   ↓                                  |
| API Request (Geolocation & Message)  |
|   ↓                    |
| Backend   |
|   ↓                    |
| Twilio API (Send SMS)  |

**Explanation:**
The frontend captures user input and location data, sends it to the backend API, which then communicates with Twilio to dispatch the alert.

---

## List of Functionalities and Verification Results
**Functionalities:**
1. SMS Alert System using Twilio API.
2. Geolocation capture with HTML5 API.
3. Minimalistic UI for quick usage.
4. Logging of sent messages for verification.

**Testing Results:**
- Functionality: Successful SMS transmission with accurate geolocation.
- Error Handling: Identified and resolved invalid phone number and location access denial issues.

---

## Achievement of Project Goals
Backend Server:
![image](https://github.com/user-attachments/assets/bf5c748e-4ceb-4565-8cac-21a263d880ce)
![image](https://github.com/user-attachments/assets/023d6f3e-5f40-4cd6-a534-a953f70b3e5e)
![image](https://github.com/user-attachments/assets/0a83b622-030b-4adb-8199-24b6bb5aa678)
![image](https://github.com/user-attachments/assets/d2cb4486-88bd-4008-a8d2-0de07379e2a0)
![image](https://github.com/user-attachments/assets/8fafcc77-5f26-454f-860f-8d8bc9ecab07)

## Discussion and Conclusions
### Issues & Limitations
- Geolocation Accuracy: Limited by device/browser capabilities.
- Twilio Constraints: SMS functionality depends on Twilio's pricing and plan.
### Learning Outcomes
This project reinforced course concepts in:
- Web development (frontend and backend integration)
- API usage (Twilio and Geolocation APIs)
- Testing and debugging
