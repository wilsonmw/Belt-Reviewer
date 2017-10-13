from django.shortcuts import render, redirect

from .models import Book, User, Author, Review
from django.contrib import messages


# Create your views here.
def index(request):
    books = Book.objects.display()
    reviews = Review.objects.all()
    context = {'books':books, 'reviews':reviews}
    return render(request, 'books_app/index.html', context)

def addPage(request):
    authors = Author.objects.all()
    context = {'authors':authors}
    return render(request, 'books_app/addPage.html', context)


def addBook(request):
    results = Author.objects.addNew(request.POST)
    if results['status']==False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/addPage')
    else:
        return redirect('/books')

def addReview(request):
    book = Book.objects.get(id=request.POST['bookname'])
    context = {
        'bookTitle':book.title,
        'id': book.id,
        'author': book.author,
    }
    return render(request, 'books_app/addReview.html', context)
