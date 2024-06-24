from rest_framework import viewsets , generics 
from Ailaysa_app.models import Book , Language , Genre
from Ailaysa_app.serializers import BookSerializer , LanguageSerializer ,GenreSerializer
from Ailaysa_app.permissions import IsStaff
from seller_auth.models import SellerUser


class BookViewSet(viewsets.ModelViewSet):
    """
    Book model viewset
    """
    queryset = Book.objects.filter(publisher=SellerUser.publisher)
    serializer_class = BookSerializer
    permission_classes = [IsStaff]

class LanguageListView(generics.ListAPIView):
    """
    Language model viewset
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    
class GenreListView(generics.ListAPIView):
    """
    Genre Model viewset
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
        
