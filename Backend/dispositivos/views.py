from rest_framework import viewsets
from .serializer import DeviceSerializer
from .models import Device
# Create your views here.

class DeviceView(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()