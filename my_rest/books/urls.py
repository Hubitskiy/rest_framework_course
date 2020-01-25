from django.urls import path
from . import views


urlpatterns = [
    path('showbooks/', views.ShowBooks.as_view(), name='showbooks'),
    path('genre/', views.BooksGenre.as_view(), name='booksgenre'),

]