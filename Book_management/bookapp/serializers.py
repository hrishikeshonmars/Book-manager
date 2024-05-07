# book_management_app/serializers.py
from rest_framework import serializers
from.models import User, Book, Author, ReadingList, ReadingListBook

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'publication_date', 'description']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class ReadingListSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = ReadingList
        fields = ['id', 'user', 'books']

class ReadingListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingListBook
        fields = ['id', 'eading_list', 'book', 'order']