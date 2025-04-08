from django.shortcuts import render
from rest_framework import viewsets
from .models import Universidad
from .serializers import UniversidadSerializer

class UniversidadViewSet(viewsets.ModelViewSet):
    queryset = Universidad.objects.all()
    serializer_class = UniversidadSerializer

# Create your views here.
