# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.timezone import now


# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, default=now)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=0)
    likes = models.ManyToManyField(User, related_name='questions', blank=True)
    def get_absolute_url(self):
        return reverse('question', kwargs={"id": self.id})
    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, default=0)
    author = models.ForeignKey(User, default=0)
