# Serializers.py
from rest_framework import serializers
from Ailaysa_app.models import Book, Author, Publisher , Language , Genre


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
    
    class Mete:
        model = Genre
        feilds = '__all__'
        