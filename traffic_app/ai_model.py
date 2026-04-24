import cv2

def detect_traffic(video_path):
    cap = cv2.VideoCapture(video_path)

    vehicle_count = 0
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Simple logic (simulate detection)
        if frame_count % 30 == 0:
            vehicle_count += 1

    cap.release()

    # Simple anomaly rule
    anomaly = True if vehicle_count > 20 else False

    return vehicle_count, anomaly
