# Serializers.py
from rest_framework import serializers
from .models import Book ,Language , Genre , FormatType

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class LanguageSerializer(serializers.ModelSerializer):
    books = BookSerializer(many = True, read_only =True)
    class meta:
        model = Language
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    books = BookSerializer(many = True, read_only =True)
    class meta:
        model = FormatType
        fields = '__all__'
        
class FormatSerializer(serializers.ModelSerializer):
    books = BookSerializer(many = True, read_only =True)
    class meta:
        model = Genre
        fields = '__all__'