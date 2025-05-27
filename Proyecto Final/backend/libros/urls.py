from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibrosViewSet

router = DefaultRouter()
router.register(r'libros', LibrosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]    