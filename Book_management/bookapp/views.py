# book_management_app/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from.models import User, Book, Author, ReadingList, ReadingListBook
from.serializers import UserSerializer, BookSerializer, AuthorSerializer, ReadingListSerializer, ReadingListBookSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken




def index(request):
    return render(request,'reading-list-management.html')

    
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookDetailView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class ReadingListView(APIView):
    def get(self, request, user_id):
        reading_lists = ReadingList.objects.filter(user_id=user_id)
        serializer = ReadingListSerializer(reading_lists, many=True)
        return Response(serializer.data)

class ReadingListDetailView(APIView):
    def get(self, request, pk):
        reading_list = ReadingList.objects.get(pk=pk)
        serializer = ReadingListSerializer(reading_list)
        return Response(serializer.data)

class ReadingListBookView(APIView):
    def post(self, request, reading_list_id, book_id):
        reading_list = ReadingList.objects.get(pk=reading_list_id)
        book = Book.objects.get(pk=book_id)
        reading_list_book = ReadingListBook(reading_list=reading_list, book=book)
        reading_list_book.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, reading_list_id, book_id):
        reading_list = ReadingList.objects.get(pk=reading_list_id)
        book = Book.objects.get(pk=book_id)
        reading_list_book = ReadingListBook.objects.get(reading_list=reading_list, book=book)
        reading_list_book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)