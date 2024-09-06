from django.db import models
from django.utils import timezone
from dispositivos.models import Device

class Reading(models.Model):
    reading_id = models.AutoField(primary_key=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)  # FK a Device
    voltage = models.DecimalField(max_digits=10, decimal_places=2)  # Ej: 220.50 V
    current = models.DecimalField(max_digits=10, decimal_places=2)  # Ej: 15.25 A
    energy = models.DecimalField(max_digits=15, decimal_places=2)   # Ej: 1000.25 kWh
    timestamp = models.DateTimeField(default=timezone.now)  # Guarda el tiempo de lectura

    def __str__(self):
        return f"Reading {self.reading_id} - Device: {self.device_id.name}"
