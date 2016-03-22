from django import forms
from django.contrib.auth.models import User

from .models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(label='Name',max_length=100, required=True)
	text = forms.CharField(label='Text Question',widget=forms.Textarea, required=True)

	# def clean():
	# 	pass 

	def save(self):
		question = Question(**self.cleaned_data)
		question.author_id=1
		question.save()
		return question.pk


class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea,label='Text',max_length=100, required=True)
	question = forms.IntegerField(label='Text Answer', widget=forms.HiddenInput, required=False)

	def __init__(self, *args, **kwargs):
		self._question = kwargs.pop('_question',None)
		forms.Form.__init__(self, *args, **kwargs)

	# def save(self):
	# 	newanswer = Answer(text=self.cleaned_data['text'], author=self.cleaned_data['author'])
	# 	newanswer.question = Question.objects.get(pk=self.cleaned_data['question'])
	# 	newanswer.save()
	# 	return self.cleaned_data['question']
	def save(self):
		self.cleaned_data['author'] = self._user
		self.cleaned_data['question'] = self._question
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer




class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, min_length=1, required=True) 
    password = forms.CharField(max_length=255, min_length=1, required=True)