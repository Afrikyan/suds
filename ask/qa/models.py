from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse


class Question(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name='question_author', blank=True, null=True)
	likes = models.ManyToManyField(User, related_name='question_likes', blank=True)

	# def get_url(self):
	# 	return reverse('question_details', kwargs={'id': self.id}
	# 		)

	def __str__(self):
		return self.title



class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User, blank=True, null=True)

