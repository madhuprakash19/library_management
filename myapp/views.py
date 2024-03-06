from django.shortcuts import render
from myapp.models import book
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    books = list(book.objects.all()) 
    return render(request,'home.html',{"books":books})


def addbook(request):
    return render(request,'addbook.html')

def edit_book(request,book_id):
    book_got = book.objects.get(id=book_id)
    print(book_got)
    return render(request,'edit_book.html',{'book_got':book_got})


def delete_book(request,book_id):
    book_got = book.objects.get(id=book_id)
    book_got.delete()
    return HttpResponseRedirect(reverse('library:home'))



def save_book(request):
    name = request.POST['name']
    book_id = request.POST['book_id']
    genre = request.POST['genre']
    author = request.POST['author']
    a = book(name=name,book_id = book_id ,genre = genre,author = author)
    a.save()
    return HttpResponseRedirect(reverse('library:home'))


def save_edited_book(request):
    books = book.objects.get(id=request.POST['id'])
    name = request.POST['name']
    book_id = request.POST['book_id']
    genre = request.POST['genre']
    author = request.POST['author']

    books.name = name
    books.book_id = book_id
    books.genre = genre
    books.author = author
    books.save()


    return HttpResponseRedirect(reverse('library:home'))

