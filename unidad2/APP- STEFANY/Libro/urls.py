from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet

router = DefaultRouter()
router.register(r'Libro', LibroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]    