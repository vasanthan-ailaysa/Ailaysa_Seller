# Serializers.py
from rest_framework import serializers
from Ailaysa_app.models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer class for Author Model
    """
    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    """
    Serializer class for Publisher Model
    """
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer class for Book model
    """
    author = AuthorSerializer(many=True)
    publisher = PublisherSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
