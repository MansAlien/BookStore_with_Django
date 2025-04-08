from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name',)

class BookSerializer(serializers.ModelSerializer):
    # For read operations, show author's name
    author_name = serializers.CharField(source='author.name', read_only=True)
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_year', 'author', 'author_name')
        extra_kwargs = {
            'author': {'write_only': True}  # author field is only for writing
        }
