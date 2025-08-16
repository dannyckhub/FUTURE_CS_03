from flask import Flask, request, render_template_string, send_file
from Crypto.Cipher import AES
import base64, os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🔑 AES key (must be 32 bytes for AES-256)
KEY = base64.b64decode("UeK8niLKP6EUmqc4RIser14NN8EceTxrxUSfBz4cD+Q=")  # example key

# Padding helpers
def pad(data):
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt_file(file_data):
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(pad(file_data)))

def decrypt_file(enc_data):
    enc_data = base64.b64decode(enc_data)
    iv = enc_data[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return cipher.decrypt(enc_data[16:]).rstrip(b"\0")

# ✅ Homepage
@app.route("/")
def index():
    return render_template_string("""
        <h2>🔐 Secure File Portal</h2>
        <p><a href='/upload'>➡️ Upload a File</a></p>
        <p>To download: open <code>/download/&lt;filename&gt;</code> after uploading.</p>
    """)

# ✅ Upload route
@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            data = file.read()
            encrypted_data = encrypt_file(data)
            filepath = os.path.join(UPLOAD_FOLDER, file.filename + ".enc")
            with open(filepath, "wb") as f:
                f.write(encrypted_data)
            return f"✅ File encrypted and uploaded as {file.filename}.enc<br><a href='/'>Back</a>"
    return render_template_string("""
        <h2>Upload File</h2>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
        <p><a href='/'>⬅️ Back to Home</a></p>
    """)

# ✅ Download route
@app.route("/download/<filename>")
def download_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            encrypted_data = f.read()
        decrypted_data = decrypt_file(encrypted_data)
        out_path = os.path.join(UPLOAD_FOLDER, "decrypted_" + filename.replace(".enc", ""))
        with open(out_path, "wb") as f:
            f.write(decrypted_data)
        return send_file(out_path, as_attachment=True)
    return "❌ File not found"

if __name__ == "__main__":
    app.run(debug=True)
