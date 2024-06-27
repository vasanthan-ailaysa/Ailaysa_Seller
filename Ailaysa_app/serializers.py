# Serializers.py
from rest_framework import serializers
from Ailaysa_app.models import Book, Language, Genre, Format


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer class for Book model
    """
    class Meta:
        model = Book
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    """
    Serializer class for Language model
    """
    class Meta:
        model = Language
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer class for Genre model
    """
    class Meta:
        model = Genre
        fields = '__all__'


class FormateSerializer(serializers.ModelSerializer):
    """
    Serializer class for Genre model
    """
    class Meta:
        model = Format
        fields = '__all__'
