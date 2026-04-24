from django.db import models

class TrafficData(models.Model):
    video = models.FileField(upload_to='uploads/', null=True, blank=True)
    vehicle_count = models.IntegerField(default=0)
    anomaly_detected = models.BooleanField(default=False)
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
      
    def __str__(self):
        return f"Traffic Data {self.id} - {self.vehicle_count} vehicles"

