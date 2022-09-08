from django.contrib import admin

from .models import *

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'publish_year')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Books, BooksAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Authors, AuthorsAdmin)
