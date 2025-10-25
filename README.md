🏧 ATM Web Application
----------------------------------------------
This is a simple ATM simulation web app built using Flask (Python) for the backend and HTML, CSS, and JavaScript for the frontend.
It allows users to register, log in, deposit, withdraw, and view their account dashboard.

🚀 Features
-----------------------------------------------
🧾 User Registration — Create a new account with username, email, password, and PIN.

🔐 User Login — Secure login using username, password, and PIN verification.

💰 Deposit Money — Deposit money into your account with validation rules:

Amount must be greater than 0

Amount must be less than ₹50,000

Amount must be a multiple of 100

💸 Withdraw Money — Withdraw funds with balance and validation checks.

🏠 Dashboard — Displays user’s name and account information after successful login.

🍪 Cookie-Based Sessions — Keeps users logged in using cookies.

🧩 Tech Stack
---------------------------
Layer	      Technology
Frontend	  HTML5, CSS3, JavaScript
Backend	    Python Flask
Templating	Jinja2
Server	    Flask’s built-in development server

⚙️ Installation & Setup
---------------------------------------
1️⃣ Clone the Repository
git clone https://github.com/yourusername/atm-flask-app.git
cd atm-flask-app

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows

3️⃣ Install Dependencies
pip install flask

4️⃣ Run the Application
python app.py

Then open your browser and visit:

http://127.0.0.1:5000/

## 📁 Project Structure
------------------------------
ATM-Flask-App/
│
├── app.py # Main Flask application file
│
├── static/ # All static frontend files
│ ├── css/
│ │ └── style.css # Main stylesheet

│ │
│ ├── js/
│ │ └── script.js # JavaScript for frontend behavior
│ │
│ └── images/ # Optional: store logo or icons
│ └── atm_logo.png
│
├── templates/ # All HTML templates
│ ├── index.html # Homepage
│ ├── Register.html # Registration form
│ ├── login.html # Login form
│ ├── home.html # User dashboard
│ ├── deposit.html # Deposit money page
│ └── withdrawal.html # Withdraw money page
│
├── README.md # Project documentation
├── .gitignore # Files to ignore by Git
└── requirements.txt # Python dependencies


🔒 Validation Rules

Deposit Rules:-
---------------------------------
Must be greater than 0

Must be less than ₹50,000

Must be a multiple of 100

Withdrawal Rules:-
----------------------------------
Must be greater than 0

Must not exceed account balance

Must be a multiple of 100

🧠 Future Improvements
---------------------------------
Add database support (e.g., SQLite or MySQL)

Implement transaction history

Add logout and password reset functionality

Enhance UI/UX design

Use Flask sessions instead of cookies for better security
