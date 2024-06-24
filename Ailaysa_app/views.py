from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from Ailaysa_app.models import Book
from Ailaysa_app.serializers import BookSerializer
from Ailaysa_app.permissions import IsStaff
from seller_auth.models import SellerUser


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(publisher=SellerUser.publisher)
    serializer_class = BookSerializer
    permission_classes = [IsStaff]

