from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for Author model with nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

