from flask import Flask, request, jsonify, render_template
from ultralytics import YOLO
from PIL import Image
from flask_cors import CORS
from io import BytesIO

app = Flask(__name__)
CORS(app)

# Load your trained model
model = YOLO("VehicleNoiseModel.pt")

# --- ADD THIS ---
# Route to serve the main HTML page
@app.route("/", methods=["GET"])
def home():
    # Renders the index.html file from the same directory
    return render_template("index.html")
# ---------------

# Noise rating function
def rate_noise(num_vehicles):
    if num_vehicles <= 2:
        return "Low"
    elif num_vehicles <= 5:
        return "Medium"
    else:
        return "High"

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    image_file = request.files["image"]
    if image_file.filename == '':
        return jsonify({"error": "No image selected for uploading"}), 400

    try:
        image_bytes = image_file.read()
        img = Image.open(BytesIO(image_bytes))
        results = model.predict(img, verbose=False)
        num_vehicles = len(results[0].boxes)
        noise_level = rate_noise(num_vehicles)

        return jsonify({
            "filename": image_file.filename,
            "num_vehicles": num_vehicles,
            "noise_level": noise_level
        })
    except Exception as e:
        return jsonify({"error": f"Error processing image: {str(e)}"}), 500

if __name__ == "__main__":
    # This part is for local development only.
    # Gunicorn will be used in production on Render.
    app.run(host="0.0.0.0", port=5000, debug=True)
