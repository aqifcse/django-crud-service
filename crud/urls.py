from django.urls import path
from . import views

urlpatterns = [
    #Author
    path('author/', views.AuthorView.as_view(), name="author"),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name="authors"),

    #Book
    # path('book/create/', views.BookView, name="book-create"),
    # path('book/read/', views.BookView, name="book-read"),
    # path('book/update/<id:int>/', views.BookDetailView, name="book-update"),
    # path('book/delete/<id:int>/', views.BookDetailView, name="book-delete")
]