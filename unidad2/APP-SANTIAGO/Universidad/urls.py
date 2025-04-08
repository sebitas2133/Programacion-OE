from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UniversidadViewSet

router = DefaultRouter()
router.register(r'universidad', UniversidadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]