from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from Ailaysa_app.models import Book, Language, Genre, Author, Publisher
from Ailaysa_app.serializers import BookSerializer, LanguageSerializer, GenreSerializer, AuthorSerializer, PublisherSerializer
from Ailaysa_app.permissions import IsStaff
from seller_auth.models import SellerUser


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
        

class AuthorListCreateView(generics.ListCreateAPIView):
    """
    Author list create view
    GET and POST endpoint
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class PublisherListCreateView(generics.ListCreateAPIView):
    """
    Publisher list create view
    GET and POST endpoint
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """
    Book model viewset
    """
    queryset = Book.objects.all()  # todo filtering
    serializer_class = BookSerializer
    permission_classes = [IsStaff]