from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutoresViewSet

router = DefaultRouter()
router.register(r'autores', AutoresViewSet)

urlpatterns = [
    path('', include(router.urls)),
]    