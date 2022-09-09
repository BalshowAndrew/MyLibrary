from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('books/', book_list, name='book_list'),
    path('books/<slug:content_slug>/', show_content, name='content'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    ]