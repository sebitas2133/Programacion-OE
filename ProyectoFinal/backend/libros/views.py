from django.shortcuts import render
from rest_framework import viewsets
from .models import Libros
from .serializers import LibrosSerializer

# Create your views here.

class LibrosViewSet(viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializer