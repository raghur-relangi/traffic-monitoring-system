import random

def detect_traffic(video_path):
    vehicle_count = random.randint(5, 50)
    anomaly = True if vehicle_count > 20 else False
    return vehicle_count, anomaly