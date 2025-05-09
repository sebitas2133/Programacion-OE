from django.shortcuts import render
from rest_framework import viewsets
from .models import Comida
from .serializers import ComidaSerializer

class ComidaViewSet(viewsets.ModelViewSet):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer
# Create your views here.
