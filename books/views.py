from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]

def index(request):
    books = Books.objects.all()

    context = {
        'books': books,
        'menu': menu,
        'title': "Главная страница",
        'cat_selected': 0,
    }
    return render(request, 'books/index.html', context=context)


def book_list(request):
    return HttpResponse('Библиотека')
