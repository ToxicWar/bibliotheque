# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.CharField(max_length=1000, verbose_name='Description', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description', blank=True)),
                ('imprint_date', models.DateField(verbose_name='Imprint date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(related_name='books', null=True, to='library.Genre', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(related_name='books', to='library.Publisher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='genres',
            field=models.ManyToManyField(related_name='authors', null=True, to='library.Genre', blank=True),
            preserve_default=True,
        ),
    ]
