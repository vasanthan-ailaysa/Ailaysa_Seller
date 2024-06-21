from django.urls import path
from Ailaysa_app.views import BookListView, BookCreateView, BookDetailView


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
