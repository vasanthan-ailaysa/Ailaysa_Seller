from django.urls import path
from Ailaysa_app.views import BookCreate, BookDetail


urlpatterns = [
    path('books/', BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
