from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pubilshed_date = models.DateField()
    genre = models.CharField(max_length=255)
