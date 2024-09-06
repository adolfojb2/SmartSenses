from django.db import models
from django.utils import timezone
from dispositivos.models import Device


class Alert(models.Model):
    ALERT_TYPES = [
        ('SOBRECONSUMO', 'Sobreconsumo'),
        ('BAJO_CONSUMO', 'Bajo_consumo'),
        ('PICO_CORRIENTE', 'Pico_corriente'),
        ('APAGON', 'Apagon'),

    ]

    alert_id = models.AutoField(primary_key=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)  # FK a Device
    type = models.CharField(max_length=15, choices=ALERT_TYPES)  # Tipo de alerta: Error, Advertencia o Información
    description = models.TextField()  # Descripción de la alerta
    timestamp = models.DateTimeField(default=timezone.now)  # Marca de tiempo de la alerta

    def __str__(self):
        return f"Alert {self.alert_id} - Device: {self.device_id.name} - Type: {self.type}"
