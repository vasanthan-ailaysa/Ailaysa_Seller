from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from Ailaysa_app.models import Book
from Ailaysa_app.serializers import BookSerializer
from Ailaysa_app.permissions import IsSeller



class BookCreate(generics.ListCreateAPIView):
    """
    view to list and create bookdata
    """

    queryset = Book.objects.all()
    serializer = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    view to retrieve, update and delete bookdata
    """

    queryset = Book.objects.all()
    serializer = BookSerializer
    permission_classes = [IsSeller]
