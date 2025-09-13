# Traffic Noise Monitoring Project 🚦🔊

## Overview
Excessive traffic contributes to noise pollution, affecting public health and quality of life. This project leverages AI and data analysis to monitor traffic intensity and estimate noise levels in real time.  

The system helps urban planners, environmental agencies, and policy makers identify noise hotspots and take preventive measures.

---
# EchoSense AI - Vehicle Noise Predictor
## Live Demo: https://trafficedu.onrender.com

A web application that uses a YOLOv8 object detection model to count vehicles in an uploaded image and estimate the corresponding urban noise level.

# Project Overview
EchoSense AI is a full-stack application designed to provide a simple yet effective way to gauge potential noise pollution from road traffic. Users can upload an image of a street or highway, and the application's backend will process it using a custom-trained YOLOv8 model to detect and count the number of vehicles. Based on this count, it classifies the traffic density and estimates the noise level as Low, Medium, or High.

This project demonstrates the end-to-end process of building and deploying a machine learning application, from the Python Flask backend to the interactive front end, all hosted on a cloud platform.

# App in Action
<!-- demo -->![Image](https://github.com/user-attachments/assets/141bc00f-f894-4a86-beda-07555623704f)

<!-- Example: -->

# Features
# Image Upload:
Interactive and user-friendly interface to select and upload road traffic images.

# Vehicle Detection:
Utilizes a custom-trained YOLOv8 model to accurately count cars, trucks, buses, and other vehicles.

# Noise Level Estimation:
Classifies the number of detected vehicles into three intuitive noise levels:

Low (0-2 Vehicles)

Medium (3-5 Vehicles)

High (6+ Vehicles)

# Dynamic UI: 
The front end instantly displays the uploaded image and the prediction results in a clean, color-coded report card.

# Fully Responsive:
The interface is designed to work seamlessly on both desktop and mobile devices.

# Tech Stack
The application is built with a modern and efficient set of technologies:

Category

Technology

Frontend

HTML5, CSS3, Vanilla JavaScript

Backend

Python, Flask (Web Framework), Gunicorn (WSGI Server)

ML Model

PyTorch, Ultralytics YOLOv8

Deployment

Git & Git LFS (for the large model file), GitHub, Render.com (PaaS)

Local Development Setup
To run this project on your local machine, follow these steps:

1. Clone the Repository:

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

2. Set Up Git LFS:
The model file is tracked using Git LFS. Make sure you have it installed.

git lfs install
git lfs pull

3. Create a Virtual Environment:
It's highly recommended to use a virtual environment to manage dependencies.

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

4. Install Dependencies:
The requirements.txt file contains all the necessary Python packages.

pip install -r requirements.txt

5. Run the Flask Application:

python app.py

The server will start, and you should see output indicating it is running on http://127.0.0.1:5000.

6. Access the Application:
Open your web browser and navigate to http://127.0.0.1:5000. You can now use the application locally.

# Deployment
This application is configured for seamless deployment on Render using an "Infrastructure as Code" approach.

The render.yaml file in the root directory contains all the build and start commands.

Render automatically detects this file, builds the environment by installing packages from requirements.txt, and starts the server using the gunicorn app:app command.

The large VehicleNoiseModel.pt file is handled by Git LFS, which Render supports natively.

Any push to the main branch on GitHub will trigger an automatic new deployment on Render.

# Project Structure
.
├── app.py                  # Main Flask application file
├── requirements.txt          # Python dependencies for pip
├── render.yaml               # Deployment instructions for Render
├── VehicleNoiseModel.pt      # The trained YOLOv8 model (tracked by Git LFS)
├── templates/
│   └── index.html            # The main HTML file for the front end
└── .gitignore                # Specifies files for Git to ignore
