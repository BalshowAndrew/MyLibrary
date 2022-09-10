from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

menu = [
    {'title': "О сайте", 'url_name': 'home'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    cats = Category.objects.all()
    context = {
        'cats': cats,
        'menu': menu,
        'title': "Главная страница",
    }
    return render(request, 'books/index.html', context=context)


def book_list(request):
    books = Books.objects.all()
    cats = Category.objects.all()

    context = {
        'books': books,
        'cats': cats,
        'menu': menu,
        'title': 'Список книг',
        # 'cat_selected': 0,
    }
    return render(request, 'books/book_list.html', context=context)


def show_content(request, slug):
    book = Books.objects.get(slug=slug)
    cats = Category.objects.all()

    context = {
        'book': book,
        'cats': cats,
        'menu': menu,
        'title': 'Статья'
    }
    return render(request, 'books/show_content.html', context=context)


def show_category(request, cat_id):
    books = Books.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {
        'books': books,
        'cats': cats,
        'menu': menu,
        'title': 'Список книг',
        # 'cat_selected': cat_slug,
    }
    return render(request, 'books/show_category.html', context=context)


def contact(request):
    cats = Category.objects.all()
    context = {
        'cats': cats,
        'menu': menu,
        'title': 'Обратная связь',
    }
    return render(request, 'books/contact.html', context=context)


def login(request):
    cats = Category.objects.all()
    context = {
        'cats': cats,
        'menu': menu,
        'title': 'Вход',
    }
    return render(request, 'books/login.html', context=context)
