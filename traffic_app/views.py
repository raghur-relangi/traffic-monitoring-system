import os
from django.shortcuts import render
from django.conf import settings
from .forms import VideoUploadForm
from .models import TrafficData
from .ai_model import detect_traffic


def index(request):
    form = VideoUploadForm()
    return render(request, 'index.html', {'form': form})


def analyze_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()

            # Use file name instead of path (Railway has no persistent storage)
            video_path = obj.video.name

            count, anomaly = detect_traffic(video_path)

            obj.vehicle_count = count
            obj.anomaly_detected = anomaly
            obj.save()

            return render(request, 'dashboard.html', {
                'count': count,
                'anomaly': anomaly
            })

    return render(request, 'index.html')