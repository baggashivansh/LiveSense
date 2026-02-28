# LiveSense

LiveSense is a real time ambient sensing system that combines computer vision with a backend event processing service.

The intention behind this project is simple: move beyond isolated object detection and toward context aware environmental intelligence.

Instead of treating vision models as standalone demos, LiveSense explores what happens when perception becomes continuous — when observations are captured, interpreted, structured, and transmitted as meaningful events. The focus is not just detection, but understanding and integration.

---

## 🌐 Live Deployment

Monitoring Interface
[https://live-sense.vercel.app](https://live-sense.vercel.app)

Backend Service
[https://livesense-backend.onrender.com/](https://livesense-backend.onrender.com/)

The live interface verifies backend availability and demonstrates real time cloud connectivity between independently deployed services.

---

## 🧠 What the System Does

LiveSense observes the physical environment through a camera feed.

A vision model detects objects such as people.
Temporal logic evaluates whether a detection is meaningful — for example, distinguishing a brief appearance from sustained presence.

When defined conditions are met, structured events are transmitted to a backend service.

The backend receives these events and provides a foundation for future storage, reasoning, analytics, or automation.

In essence, LiveSense acts as a perception layer for building context aware applications.

---

## 🏗 Architecture Overview

LiveSense is organized into three clear layers:

### Vision Sensing Layer

A Python based service using OpenCV and YOLO.
Captures live camera frames.
Performs object detection.
Tracks detection duration to identify meaningful presence.

### Event Transmission Layer

Structured JSON events.
HTTP based communication.
Instead of sending raw video, the system transmits interpreted observations.

### Backend Processing Layer

Spring Boot application.
Receives typed events.
Designed to evolve into a persistence, reasoning, and automation layer.

The monitoring interface hosted on Vercel validates backend availability and demonstrates cross platform cloud communication in a distributed setup.

---

## ⚙️ Current Capabilities

* Real time person detection
* Continuous presence evaluation based on duration
* Event based communication between vision and backend
* Structured event ingestion on backend
* Cloud deployment across independent platforms

---

## 🔭 Why This Project Exists

Many AI projects stop at showcasing model accuracy.

LiveSense focuses on system integration.

Real intelligence does not emerge from isolated predictions.
It emerges from continuous sensing, temporal reasoning, memory, and structured decision pipelines.

This project is a foundational step toward ambient computing systems where digital services adapt dynamically to real world context.

---

## 🔍 Broader Exploration

LiveSense is part of a deeper exploration into vision systems and intelligent agents.

Related article:
[https://baggashivansh.hashnode.dev/building-realtime-vision-ai-with-vision-agents](https://baggashivansh.hashnode.dev/building-realtime-vision-ai-with-vision-agents)

The article expands on the architectural thinking behind real time perception systems and how they can evolve into intelligent agent driven environments.

---

## 🚀 Project Status

LiveSense is currently in an experimental phase focused on validating architecture and cloud connectivity.

The core sensing and event transmission pipeline is operational.
Future work will focus on persistence, reasoning layers, and intelligent automation.

---

Built by **Shivansh Bagga**
