# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.CharField(max_length=20)
    likes = models.ForeignKey(User)

class Answer(models.Model):
    text = models.CharField(max_length=100)
    added_at = models.DateField()
    question = models.OneToOneField(Question)
    author = models.CharField(max_length=20)
