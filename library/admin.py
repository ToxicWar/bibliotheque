# coding: utf-8
from __future__ import unicode_literals
from django.contrib import admin
from .models import Book, Author, Publisher, Genre


admin.site.register(Book, admin.ModelAdmin)
admin.site.register(Author, admin.ModelAdmin)
admin.site.register(Publisher, admin.ModelAdmin)
admin.site.register(Genre, admin.ModelAdmin)
