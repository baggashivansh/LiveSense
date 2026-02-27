import cv2

cam = cv2.VideoCapture(0)

while True:
    ok, frame = cam.read()
    if not ok:
        break

    cv2.imshow("LiveSense Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()