from django import forms
from .models import TrafficData

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = TrafficData
        fields = ['video']
