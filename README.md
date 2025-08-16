# FUTURE_CS_03
Secure file upload/download portal with AES encryption using Flask.

🔐 Secure File Upload/Download Portal with AES Encryption

This project is a Flask-based web portal that allows users to securely upload and download files.
All uploaded files are encrypted using AES (Advanced Encryption Standard) before being stored, ensuring security at rest and in transit.

🚀 Features

🔒 AES Encryption (CBC mode) → Files are encrypted before storage

🗝️ Unique encryption key per session (using PyCryptodome)

📤 Upload files securely via web form or API (curl/Postman)

📥 Download & decrypt files on request

📂 Organized storage of encrypted and decrypted files

🌐 Flask API endpoints for integration and testing

🔧 Tools & Technologies

Python 3.x

Flask → Web framework

PyCryptodome → AES encryption library

HTML/CSS (Bootstrap) → Simple frontend UI

curl / Postman → API testing tools

Git & GitHub → Version control and repository hosting

📂 Project Structure
FlaskAES/
│── app.py                # Main Flask application
│── requirements.txt      # Python dependencies
│── uploads/              # Stores encrypted files
│── decrypted/            # Stores decrypted files
│── templates/
│     └── index.html      # Upload/Download UI
│── README.md             # Project documentation

⚡ Setup & Run

Clone the repository

git clone https://github.com/dannyckhub/flask-aes-portal.git
cd flask-aes-portal


Create & activate virtual environment

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac


Install dependencies

pip install -r requirements.txt


Run the Flask app

python app.py


Access in browser
👉 http://127.0.0.1:5000

📤 Upload a File (via curl/Postman)
curl -X POST -F "file=@test.txt" http://127.0.0.1:5000/upload


✔️ File will be encrypted and stored in uploads/

📥 Download & Decrypt File
curl -X GET "http://127.0.0.1:5000/download?filename=test.txt.enc" --output decrypted.txt


✔️ File will be decrypted and saved as decrypted.txt

🛡️ Security Highlights

AES-CBC mode with PKCS7 padding

Random IV (Initialization Vector) for every encryption

Separation of encrypted vs. decrypted files

API endpoints for automation and testing

🛠 Skills Demonstrated

Flask backend development

File handling (upload/download in web apps)

AES encryption with PyCryptodome

API testing using curl/Postman

Secure coding & project structuring
