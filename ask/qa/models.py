from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):                                          
        def new():                                                              
                pass                                                            
        def popular():                                                          
                pass 
            
class Question(models.Model):
    class Question(models.Model):                                                   
        objects = QuestionManager() 
    title = models.CharField(max_length=200)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True,default=now())
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='question_author', default=1)
    likes = models.ManyToManyField(User, related_name='question_likes', default=0)

    def get_absolute_url(self):
        return reverse('question', kwargs={"id": self.id})

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True,default=now())
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, default=1, null=True)

