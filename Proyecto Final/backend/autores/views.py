from django.shortcuts import render
from rest_framework import viewsets
from .models import Autores
from .serializers import AutoresSerializer

# Create your views here.

class AutoresViewSet(viewsets.ModelViewSet):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer