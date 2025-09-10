import os
import csv
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
# Capture form submission
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
# Run Flask app
# ------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

