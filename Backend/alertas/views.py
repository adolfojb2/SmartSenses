from rest_framework import viewsets
from .serializer import AlertSerializer
from .models import Alert
# Create your views here.

class AlertView(viewsets.ModelViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()