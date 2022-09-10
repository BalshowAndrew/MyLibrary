from django.db import models
from django.urls import reverse


class Books(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Описание книги')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления в каталог')
    publish_year = models.IntegerField(verbose_name='Гов издания')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')
    auth = models.ManyToManyField('Authors', related_name='books')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books', kwargs={'title_slug': self.slug})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категории')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Authors(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Автор')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    country = models.CharField(max_length=50, db_index=True, verbose_name='Страна')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('authors', kwargs={'auth_slug': self.slug})

    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Авторы'
