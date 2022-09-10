from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('books/', book_list, name='book_list'),
    path('books/<slug:slug>/', show_content, name='content'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    ]