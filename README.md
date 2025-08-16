# FUTURE_CS_03
Secure file upload/download portal with AES encryption using Flask.

Flask AES File Portal

A simple file upload/download portal built with Flask and AES encryption using PyCryptodome.
This project secures files both at rest (on disk) and in transit (via HTTPS if deployed with TLS).

🔧 Features

Upload files securely via web form or curl/Postman

Files encrypted with AES (CBC mode) before storage

Download & automatic decryption of files

Works locally or can be deployed on any server

📂 Project Structure
FlaskAES/
│── app.py              # Main Flask application  
│── requirements.txt    # Dependencies (Flask, pycryptodome)  
│── uploads/            # Stores encrypted & decrypted files  
│── README.md           # Project documentation  

⚡ Installation & Setup

Clone repo

git clone https://github.com/dannyckhub/flask-aes-portal.git
cd flask-aes-portal


Create virtual environment

python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Linux/Mac


Install dependencies

pip install -r requirements.txt


Run the app

python app.py


Visit in browser:
👉 http://127.0.0.1:5000

📤 Upload Example (via curl)
curl -X POST -F "file=@example.txt" http://127.0.0.1:5000/upload

📥 Download Example
curl -O http://127.0.0.1:5000/download/example.txt

🔒 Security Notes

AES key is generated once per session in this demo.

For production:

Use a persistent key (stored securely, e.g., in an environment variable).

Deploy with HTTPS (TLS) to secure data in transit.

Add authentication before allowing uploads/downloads.

🛠 Tools & Skills Demonstrated

Flask (Python web framework)

PyCryptodome (AES encryption/decryption)

Git & GitHub (version control & project hosting)

Postman / curl (API testing)
