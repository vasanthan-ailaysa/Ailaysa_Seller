from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Ailaysa_app.views import BookViewSet, LanguageListView, GenreListView, AuthorListCreateView, PublisherListCreateView

# register router
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('language/', LanguageListView.as_view(), name='language'),
    path('genre/', GenreListView.as_view(), name='genre'),
    path('author/', AuthorListCreateView.as_view(), name='author'),
    path('publisher/', PublisherListCreateView.as_view(), name='publisher'),
]
