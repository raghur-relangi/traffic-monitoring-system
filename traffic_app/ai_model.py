import os
os.environ["DISPLAY"] = ""
os.environ["OPENCV_VIDEOIO_PRIORITY_BACKEND"] = "0"
os.environ["QT_QPA_PLATFORM"] = "offscreen"
cv2.setNumThreads(0)

import cv2

def detect_traffic(video_path):
    cap = cv2.VideoCapture(video_path, cv2.CAP_FFMPEG)

    vehicle_count = 0
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        if frame_count % 30 == 0:
            vehicle_count += 1

    cap.release()

    anomaly = True if vehicle_count > 20 else False

    return vehicle_count, anomaly