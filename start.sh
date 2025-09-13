#!/bin/bash

# ---------------------------------------
# Vehicle Noise App - Backend Startup Script
# ---------------------------------------

# Activate virtual environment if you have one (optional)
# Uncomment and change path if you use venv
# source venv/bin/activate

# Set Flask app environment variables
export FLASK_APP=app.py
export FLASK_ENV=production  # use 'development' if debugging locally

# Run Flask app on all network interfaces, port 5000
flask run --host=0.0.0.0 --port=5000
