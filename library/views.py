# coding: utf-8
from __future__ import unicode_literals
from django.views.generic import TemplateView
from .models import Book, Author, Genre, Publisher


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['authors'] = Author.objects.all()
        context['genres'] = Genre.objects.all()
        context['publishers'] = Publisher.objects.all()
        return context

home = Home.as_view()
