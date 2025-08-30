# Traffic Noise Monitoring Project 🚦🔊

## Overview
Excessive traffic contributes to noise pollution, affecting public health and quality of life. This project leverages AI and data analysis to monitor traffic intensity and estimate noise levels in real time.  

The system helps urban planners, environmental agencies, and policy makers identify noise hotspots and take preventive measures.

---

## Dataset
https://drive.google.com/open?id=19auDxv5fLeI4pyU2114xmNJaPH8x7S-r
- **Traffic images/videos** collected from city cameras.  
- **Noise level readings** captured using sound sensors or decibel meters.  
- **Data attributes**: timestamps and locations for correlation with traffic patterns.  

---

## Key Features
- Traffic density monitoring  
- Vehicle type classification (car, bus, truck, motorcycle, bicycle)  
- Noise level measurement and correlation  

---

## Technologies Used
- **Programming Language**: Python  
- **Deep Learning Framework**: YOLOv8 (Ultralytics) for vehicle detection  
- **Data Analysis & Visualization**: Pandas, NumPy, Matplotlib  
- **Image Processing**: OpenCV  

---

## Project Highlights
- Detects traffic flow and vehicle types from images/videos.  
- Correlates traffic rate with noise levels.  
- Generates visualizations and heatmaps of noisy areas.  
- Can be extended for smart city noise management.

---

## How to Run
1. Clone this repository.  
2. Upload traffic images/videos and sensor data.  
3. Preprocess images and organize datasets by time or location.  
4. Train the YOLO model to detect vehicles.  
5. Analyze traffic density and noise correlation using provided scripts.  
6. Visualize traffic and noise trends using Matplotlib.  

---

## Results & Future Work
- Can identify high-noise traffic zones in real time.  

**Future improvements:**  
- Integrate with IoT sensors for live monitoring.  
- Predict noise levels based on traffic patterns.  
- Deploy as a dashboard for city authorities.  
