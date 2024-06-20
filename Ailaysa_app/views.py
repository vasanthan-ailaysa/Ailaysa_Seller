from django.shortcuts import render

# views.py

from rest_framework import generics
from .models import Book, Language, Genre, FormatType
from .serializers import BookSerializer, LanguageSerializer, GenreSerializer, FormatSerializer

class BookCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer


class LanguageCreate(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer = LanguageSerializer


class GenreCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer = GenreSerializer

class FormatCreate(generics.ListCreateAPIView):
    queryset = FormatType.objects.all()
    serializer = FormatSerializer

class FormatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormatType.objects.all()
    serializer = FormatSerializer

