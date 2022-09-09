from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

menu = [
    {'title': "О сайте", 'url_name': 'home'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    context = {
        'menu': menu,
        'title': "Главная страница",
    }
    return render(request, 'books/index.html', context=context)


def book_list(request):
    books = Books.objects.all()

    context = {
        'books': books,
        'menu': menu,
        'title': 'Список книг',
    }
    return render(request, 'books/book_list.html', context=context)


def show_content(request, content_slug):
    context = {
        'menu': menu,
        'title': 'Статья'
    }
    return render(request, 'books/show_content.html', context=context)



def contact(request):
     context = {
         'menu': menu,
         'title': 'Обратная связь',
     }
     return render(request, 'books/contact.html', context=context)


def login(request):
    context = {
        'menu': menu,
        'title': 'Вход',
    }
    return render(request, 'books/login.html', context=context)
