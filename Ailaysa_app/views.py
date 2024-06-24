from rest_framework import viewsets
from Ailaysa_app.models import Book
from Ailaysa_app.serializers import BookSerializer
from Ailaysa_app.permissions import IsStaff
from seller_auth.models import SellerUser


class BookViewSet(viewsets.ModelViewSet):
    """
    Book model viewset
    """
    queryset = Book.objects.filter(publisher=SellerUser.publisher)
    serializer_class = BookSerializer
    permission_classes = [IsStaff]
