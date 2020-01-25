from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class BooksModel(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    author = models.CharField(max_length=30)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


# Create your models here.
