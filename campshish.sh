#!/bin/bash

# Step 1: Clone the repo (only if not already cloned)
if [ ! -d "cybersecurity-tools-camphisher" ]; then
    echo "Cloning the repository..."
    git clone https://github.com/Masumoou/cybersecurity-tools-camphisher.git
fi

# Step 2: Navigate into the repo folder
cd cybersecurity-tools-camphisher

# Step 3: Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Step 4: Activate the virtual environment
source venv/bin/activate

# Step 5: Install required dependencies (from requirements.txt)
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 6: Run the app
echo "Running the Flask app..."
python app.py

