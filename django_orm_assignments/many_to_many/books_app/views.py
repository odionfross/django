from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'index.html', context)

def create_book(request):
    if request.method == 'POST':
        Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc']
        )
        return redirect('/')
    return redirect('/')

def view_book(request, book_id):
    context = {
        'one_book': Book.objects.get(id=book_id),
        'select_authors': []
    }
    # only include authors not yet associated with the book
    for author in Author.objects.all():
        if author not in context['one_book'].authors.all():
            context['select_authors'].append(author)
    return render(request, 'book.html', context)

def add_author_to_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author'])
    author.books.add(book)
    return redirect(f"/books/{book_id}")

def authors(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'author.html', context)

def create_author(request):
    if request.method == 'POST':
        Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
        )
        return redirect('/authors')
    return redirect('/authors')

def view_author(request, author_id):
    context = {
        'one_author': Author.objects.get(id=author_id),
        'select_books': Book.objects.exclude(id=author_id)
    }
    # only include books not yet associated with the author
    # the for loop handles the exclusion in the view where as the books exclusion can be done in the djago query as shown above
    # for book in Book.objects.all():
    #     if book not in context['one_author'].books.all():
    #         context['select_books'].append(book)
    return render(request, 'one_author.html', context)

def add_book_to_author(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['book'])
    author.books.add(book) # add book to author
    return redirect(f"/authors/{author_id}")