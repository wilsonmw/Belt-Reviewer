from __future__ import unicode_literals

from django.db import models
from ..beltreviewer_app.models import User

# Create your models here.
class BookManager(models.Manager):
    def display(self):
        books = Book.objects.all()
        return books


class AuthorManager(models.Manager):
    def addNew(self, postData):
        results = {'errors':[], 'status':True}
        if postData['author']:
            author = Author.objects.filter(name=postData['author'])
            if len(author)!=0:
                results['errors'].append("That author is already in the system. Please choose from the drop down list.")
                results['status']=False
                return results
            else:
                Author.objects.create(name=postData['author'])
                author = Author.objects.get(name=postData['author'])
                Book.objects.create(title=postData['title'], author=author)
                book = Book.objects.get(title=postData['title'])
                Review.objects.create(content=postData['review'], book = book)
                return results

class ReviewManager(models.Manager):
    def test(self):
        return self

class Author(models.Model):
    name = models.CharField(max_length=100)
    objects = AuthorManager()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

