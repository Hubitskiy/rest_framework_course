from rest_framework import serializers
from books.models import Genre, BooksModel
from django.contrib.auth.models import User


class UserSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class GenreSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('title',)

class BookModelSerializerAPI(serializers.ModelSerializer):
    genre = GenreSerializerAPI()
    publisher = UserSerializerAPI()
    class Meta:
        model = BooksModel
        fields = '__all__'

class BooksSerializerAPIPOST(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = ("title", "text", "author", "publisher", "genre")
