from django.http import HttpResponse
from django.shortcuts import render
from library.models import Books
from library.models import BookImageAndFile
from .forms import BooksForm

def library(request):
    books = Books.objects.all()
    ImagesAndFile = BookImageAndFile.objects.all()
    form = BooksForm(request.POST or None)
    return render(request, 'library/index.html',locals())