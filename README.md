# 🏦 ATM Web Application (Flask + MySQL Integration)

A responsive **ATM Simulation Web App** built using **Flask**, **HTML**, **CSS**, and **JavaScript**, featuring user registration, login, deposit, withdrawal, balance check, and mini statements.

The current version stores data in-memory for demonstration, while the **next update will include full MySQL database integration** for persistent user accounts and transactions.

---

## 📁 Project Structure

ATM_WEBAPP/
│
├── app.py # Main Flask backend
│
├── static/
│ ├── css/
│ │ ├── index.css # Landing page
│ │ ├── login.css # Login page styles
│ │ ├── register.css # Registration page
│ │ ├── home.css # Dashboard layout
│ │ ├── amount.css # Deposit & Withdraw forms
│ │ ├── balance.css # Balance display
│ │ └── statements.css # Mini statements table
│ │
│ └── assets/
│ ├── login.webp
│ ├── register.webp
│ ├── dashboard.png
│ └── deposit.jpg
│
├── templates/
│ ├── index.html
│ ├── Register.html
│ ├── login.html
│ ├── home.html
│ ├── deposit.html
│ ├── withdrawal.html
│ ├── balance.html
│ └── statement.html
│
└── README.md


---

## 🚀 Features

### 🔐 User Authentication
- Create accounts with **username, email, password, and 4-digit PIN**
- Secure login with password + PIN validation
- Uses cookies for session management

### 💰 Deposit Funds
- Accepts multiples of ₹100 (limit ₹50,000 per transaction)
- Validates user input and updates balance dynamically

### 💸 Withdraw Funds
- Ensures sufficient balance before withdrawal
- Enforces ₹50,000 limit and ₹100 multiples rule

### 💳 Check Balance
- Displays user’s available balance instantly

### 📜 Mini Statements
- Displays detailed deposit and withdrawal history with timestamps

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/ATM_WEBAPP.git
cd ATM_WEBAPP

2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

3. Install dependencies
pip install flask mysql-connector-python

4. Run the app
python app.py

5. Open in browser
http://127.0.0.1:5000/

🧠 Backend Flow (Flask + Future MySQL)
Current Implementation:

User data stored in dictionaries:

users = {}
statements = {}

Future Implementation (MySQL):

Data will be persisted using MySQL database:

users table → stores username, email, password, pin, and balance

transactions table → logs deposit and withdrawal operations with timestamps

🧩 Tech Stack
| Layer              | Technology              |
| ------------------ | ----------------------- |
| Backend            | Flask (Python)          |
| Frontend           | HTML5, CSS3, JavaScript |
| Database (Future)  | MySQL                   |
| Template Engine    | Jinja2                  |
| Session Management | Cookies                 |

Cookies
🧠 Learning Objectives

Build full-stack applications using Flask

Handle forms, routes, and dynamic HTML rendering

Implement CRUD operations with MySQL (future update)

Design responsive UI using modular CSS

Manage sessions securely using cookies

🧑‍💻 Author

Shaik Irfan
Python & Flask Developer | Passionate about scalable web applications

📍 Tenali, Andhra Pradesh

🪪 License

This project is open-source under the MIT License.
Feel free to use, modify, and improve it.

🌟 Future Roadmap

✅ Flask base version (in-memory)
🛠️ Next: Integrate MySQL with flask-mysqldb or mysql-connector
🧾 Add transaction filtering (by date, type)
🔐 Encrypt passwords using bcrypt
📊 Add admin dashboard for monitoring transactions

💬 Feedback

If you find this project helpful, please ⭐ it on GitHub.
Your support motivates the next version with full MySQL database support!

