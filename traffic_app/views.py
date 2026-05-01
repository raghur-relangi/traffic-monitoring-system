from django.shortcuts import render
from .forms import VideoUploadForm
from .ai_model import detect_traffic


def index(request):
    form = VideoUploadForm()
    return render(request, 'index.html', {'form': form})


def analyze_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            count, anomaly = detect_traffic(None)
            return render(request, 'dashboard.html', {
                'count': count,
                'anomaly': anomaly
            })
    return render(request, 'index.html')