import cv2
import requests
import time
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

BACKEND_URL = "http://localhost:8080/vision/events"
CONF_THRESHOLD = 0.75
COOLDOWN = 3

cap = cv2.VideoCapture(0)

last_sent = 0
event_count = 0

print("LiveSense AI started")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)

    for r in results:
        for box in r.boxes:
            conf = float(box.conf[0])
            if conf < CONF_THRESHOLD:
                continue

            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame,
                        f"{label} {conf:.2f}",
                        (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0,255,0),
                        2)

            now = time.time()
            if now - last_sent > COOLDOWN:
                payload = {
                    "cameraId": "cam01",
                    "eventType": label + "Detected",
                    "confidence": conf
                }

                try:
                    requests.post(BACKEND_URL, json=payload)
                    event_count += 1
                    print("Event sent:", payload)
                except:
                    print("Backend unreachable")

                last_sent = now

    cv2.putText(frame,
                f"LiveSense | Events: {event_count}",
                (10, frame.shape[0]-20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255,255,255),
                2)

    cv2.imshow("LiveSense AI Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()