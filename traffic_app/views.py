import os
from django.shortcuts import render
from django.conf import settings
from .forms import VideoUploadForm
from .models import TrafficData
from .ai_model import detect_traffic


# Home Page
def index(request):
    form = VideoUploadForm()
    return render(request, 'index.html', {'form': form})


# Video Analyze
def analyze_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()

            video_path = obj.video.path

            # AI processing
            count, anomaly = detect_traffic(video_path)

            # Save results
            obj.vehicle_count = count
            obj.anomaly_detected = anomaly
            obj.save()

            return render(request, 'dashboard.html', {
                'count': count,
                'anomaly': anomaly
            })

    return render(request, 'index.html')
