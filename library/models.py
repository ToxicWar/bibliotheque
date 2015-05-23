# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Book(models.Model):
    title = models.CharField('Title', max_length=255)
    description = models.CharField('Description', max_length=1000, blank=True)
    authors = models.ManyToManyField('Author', related_name='books', blank=True, null=True)
    genres = models.ManyToManyField('Genre', related_name='books', blank=True, null=True)
    publisher = models.ForeignKey('Publisher', related_name='books')
    imprint_date = models.DateField('Imprint date')

    def get_genres(self):
        return ', '.join([genre.title for genre in self.genres.all()])

    def get_authors(self):
        return ', '.join([author.name for author in self.authors.all()])

    def __unicode__(self):
        return self.title


class Author(models.Model):
    name = models.CharField('Name', max_length=255)
    description = models.CharField('Description', max_length=1000, blank=True)
    genres = models.ManyToManyField('Genre', related_name='authors', blank=True, null=True)

    def get_genres(self):
        return ', '.join([genre.title for genre in self.genres.all()])

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField('Title', max_length=255)

    def __unicode__(self):
        return self.title


class Publisher(models.Model):
    title = models.CharField('Title', max_length=255)
    city = models.CharField('City', max_length=100)

    def __unicode__(self):
        return self.title
