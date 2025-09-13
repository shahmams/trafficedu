import requests

url = "http://127.0.0.1:5000/predict"
image_path = "C:/Users/shahm/Downloads/sample.jpg"  # update with your image path

with open(image_path, "rb") as img:
    files = {"image": img}
    response = requests.post(url, files=files)

print("Response from server:", response.text)

