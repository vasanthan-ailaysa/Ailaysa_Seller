from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from Ailaysa_app.models import Book, Language, Genre, Author, Publisher
from Ailaysa_app.serializers import BookSerializer, LanguageSerializer, GenreSerializer, AuthorSerializer, PublisherSerializer
from Ailaysa_app.permissions import IsStaff


class LanguageListView(generics.ListAPIView):
    """
    Language list view
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    
class GenreListView(generics.ListAPIView):
    """
    Genre list view
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PublisherListCreateView(generics.ListCreateAPIView):
    """
    View to list all publishers
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class AuthorListCreateView(generics.ListCreateAPIView):
    """
    Author list create view
    GET and POST endpoint
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """
    Book model view set
    """

    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsStaff]

    def get_queryset(self):
        return Book.objects.filter(publisher=self.request.user.publisher)
