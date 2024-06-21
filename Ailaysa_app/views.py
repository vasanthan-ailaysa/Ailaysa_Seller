from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from Ailaysa_app.models import Book
from Ailaysa_app.serializers import BookSerializer
from Ailaysa_app.permissions import IsSeller



class BookListView(generics.ListAPIView):
    """
    view to list bookdata
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookCreateView(generics.ListAPIView):
    """
    view to create bookdata
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsSeller]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    view to retrieve, update and delete bookdata
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsSeller]
