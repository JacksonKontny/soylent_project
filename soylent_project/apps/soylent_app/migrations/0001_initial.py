# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nDB_No', models.IntegerField()),
                ('minimum', models.IntegerField()),
                ('maximum', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LimitRequirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nutr_No', models.IntegerField()),
                ('maximum', models.BooleanField()),
                ('limit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=128)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RatioRequirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nutr_No1', models.IntegerField()),
                ('nutr_No2', models.IntegerField()),
                ('numerator', models.IntegerField()),
                ('denominator', models.IntegerField()),
                ('maximum', models.BooleanField()),
                ('profile', models.ForeignKey(to='soylent_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=128)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='limitrequirement',
            name='profile',
            field=models.ForeignKey(to='soylent_app.Profile'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(to='soylent_app.Recipe'),
        ),
    ]
