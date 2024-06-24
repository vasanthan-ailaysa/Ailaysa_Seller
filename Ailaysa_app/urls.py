from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Ailaysa_app.views import BookViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
