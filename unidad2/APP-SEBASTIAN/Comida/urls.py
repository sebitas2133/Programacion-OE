from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComidaViewSet

router = DefaultRouter()
router.register(r'Comida', ComidaViewSet)

urlpatterns = [
    path('', include(router.urls))
]