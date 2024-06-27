from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from Ailaysa_app.models import Book, Language, Genre, Format
from Ailaysa_app.serializers import BookSerializer, LanguageSerializer, GenreSerializer, FormatSerializer


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


class FormatListView(generics.ListAPIView):
    """
    Format list view
    """
    queryset = Format.objects.all()
    serializer_class = FormatSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    Book model view set
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
