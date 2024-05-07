# book_management_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author')
    genre = models.CharField(max_length=255)
    publication_date = models.DateField()
    description = models.TextField(blank=True, null=True)

class Author(models.Model):
    name = models.CharField(max_length=255)

class ReadingList(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    books = models.ManyToManyField('Book', through='ReadingListBook')

class ReadingListBook(models.Model):
    reading_list = models.ForeignKey('ReadingList', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    order = models.IntegerField()