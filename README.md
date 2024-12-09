# 📢 Emergency Communication System

---

## 🚀 **Project Overview**

The **Emergency Communication System** is a web-based application that allows users to send emergency alerts via SMS using Twilio. Users can capture their geolocation using HTML5's Geolocation API to provide additional context about their emergency. This system is designed to be simple, intuitive, and efficient, enabling users to send alerts with just a few clicks.

---

## 📜 **Table of Contents**

1. [Project Title & Overview](#project-title--overview)  
2. [Technologies Used](#technologies-used)  
3. [Setup Instructions](#setup-instructions)  
4. [Usage Instructions](#usage-instructions)  
5. [API Reference](#api-reference)  
6. [System Features](#system-features)  
7. [Geolocation Integration Explanation](#geolocation-integration-explanation)  
8. [Troubleshooting](#troubleshooting)  
9. [Future Features](#future-features)  
10. [Acknowledgments](#acknowledgments)

---

## 💻 **Technologies Used**

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
