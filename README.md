# LiveSense AI Monitoring System

LiveSense is a real time AI powered vision monitoring system that detects objects using computer vision and converts them into structured detection events.

Instead of just showing a video feed, LiveSense transforms visual data into meaningful events that can be stored, tracked and monitored through a live dashboard.

This project demonstrates a complete AI pipeline from camera to dashboard.

---

## The Idea

Most surveillance systems only record video.
They do not understand what is happening.

LiveSense adds intelligence on top of video by:

* Detecting objects in real time
* Generating structured detection events
* Storing them in a backend system
* Displaying them on a live dashboard

It bridges computer vision with backend engineering.

---

## How It Works

The system follows a clean modular architecture:

Camera
→ YOLOv8 AI engine (Python)
→ Spring Boot REST API
→ H2 Database
→ Live Dashboard

Each layer is independent and scalable.

The AI engine detects objects and sends structured JSON events to the backend.
The backend stores events in a database.
The dashboard polls the backend and displays live detection activity.

---

## Tech Stack

Backend

* Java 17
* Spring Boot
* Spring Data JPA
* H2 In Memory Database

AI Engine

* Python 3
* Ultralytics YOLOv8
* OpenCV

Frontend

* HTML
* Modern CSS
* REST API polling

---

## Project Structure

LiveSense
backend
vision
index.html

The backend handles event storage.
The vision module handles AI detection.
The dashboard visualizes events in real time.

---

## How To Run

Step 1: Start Backend

cd backend
./mvnw clean spring-boot:run

Open in browser:
[http://localhost:8080/vision/events](http://localhost:8080/vision/events)

If you see an empty JSON array, backend is running correctly.

---

Step 2: Start AI Vision Engine

cd vision
python3 vision.py

Your camera window will open.
When objects are detected, events will be sent to the backend.

---

Step 3: Start Dashboard

From project root:

python3 -m http.server 5500

Open in browser:
[http://localhost:5500](http://localhost:5500)

Click Start.
You will see live detection events updating in the dashboard.

---

## Example Event

{
"cameraId": "cam01",
"eventType": "personDetected",
"confidence": 0.92,
"timestamp": "2026-02-27T11:57:24.228990Z"
}

---

## Key Highlights

* Real time object detection
* Event based backend processing
* Database persistence
* Clean modular architecture
* Modern monitoring dashboard
* Clear separation of concerns

This is not just object detection.
It is a complete AI monitoring pipeline.

---

## Future Improvements

* WebSocket real time streaming
* Multi camera support
* Cloud deployment
* Alert system integration
* Analytics dashboard
* Gesture based controls

---

LiveSense demonstrates how AI can move beyond experimentation and integrate into real backend systems.

Built by Shivansh Bagga
