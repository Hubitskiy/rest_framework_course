from django.contrib import admin
from .models import Genre, BooksModel


class BooksModelAdmin(admin.ModelAdmin):
    fields = ("title", "text", "author", "publisher", "genre")

admin.site.register(BooksModel, BooksModelAdmin)
admin.site.register(Genre)
# Register your models here.
