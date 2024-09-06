from rest_framework import viewsets
from .serializer import ReadingSerializer
from .models import Reading
# Create your views here.

class ReadingView(viewsets.ModelViewSet):
    serializer_class = ReadingSerializer
    queryset = Reading.objects.all()