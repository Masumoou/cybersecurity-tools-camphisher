# Cybersecurity Tools - CamPhisher

CamPhisher is a phishing simulation tool that allows you to simulate phishing attacks for educational purposes. The tool provides a login page that captures submitted data and a camera page that allows users to capture images (e.g., for testing purposes).

## Features

- **Login Simulation**: Simulate phishing login pages and capture submitted data.
- **Camera Access**: Capture snapshots using the webcam, and save the captured images to the server.
- **Data Capture**: All captured data (including login submissions and camera images) is saved locally in a CSV file and image directory.

---

## Requirements

- Python 3.x
- pip (Python package installer)

---

## Setup

Follow the steps below to set up the project on your local machine:

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/Masumoou/cybersecurity-tools-camphisher.git
cd cybersecurity-tools-camphisher
2. Create a Virtual Environment
Create a virtual environment to isolate dependencies:

bash
Copy code
python3 -m venv venv
3. Activate the Virtual Environment
Activate the virtual environment:

bash
Copy code
source venv/bin/activate
4. Install Dependencies
Install the necessary dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Application
After setting up the environment, you can run the Flask app:

bash
Copy code
python app.py
The app will be running at http://127.0.0.1:8080.

Accessing the Pages:
Login Page: http://127.0.0.1:8080/login

Camera Page: http://127.0.0.1:8080/camera

Camera Access
The camera page allows you to capture images using your webcam. The images will be saved to the server under the data/ folder with unique filenames based on the timestamp.

Data Storage
Captured Data: The login data is saved to a CSV file in the data/ folder.

Captured Images: Images captured from the camera are saved as PNG files in the data/ folder.

Troubleshooting
If you encounter any issues with camera access, make sure your browser has camera permissions enabled.

If dependencies are missing, try re-running pip install -r requirements.txt to install them again.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contribution
If you'd like to contribute to this project, feel free to fork the repository, submit issues, or create pull requests. Please ensure that you follow best practices for secure coding and documentation.

yaml
Copy code

---

### Instructions to Create the `README.md`:

1. Go to your project folder:
   ```bash
   cd ~/cybersecurity-tools-camphisher
