from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
    path('create_book', views.create_book),
    path('books/<int:book_id>', views.view_book),
    path('add_author_to_book/<int:book_id>', views.add_author_to_book),
    path('authors', views.authors),
    path('create_author', views.create_author),
    path('authors/<int:author_id>', views.view_author),
    path('add_book_to_author/<int:author_id>', views.add_book_to_author)
]