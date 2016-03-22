# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.decorators.http import require_GET, require_POST

from .models import Question, Answer
from .forms import AskForm, AnswerForm, SignupForm, LoginForm


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def test(request, *args, **kwargs):
	return HttpResponse('OK')


def home_page(request):
	questions = Question.objects.order_by('-id')
	paginator = Paginator(questions, 10)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
	      	queryset = paginator.page(paginator.num_pages)

	context = {
	    'questions': queryset,
	 }
	return render(request,'index.html', context)
	


@login_required(login_url='/login/')
def question_details(request, id):
	question = get_object_or_404(Question, id=int(id))

	if request.method == 'POST':
		form = AnswerForm(request.POST, _question=question)
		form._user = request.user
		if form.is_valid():
			answer = form.save()
			answer._user = request.user
			return HttpResponseRedirect('/question/{}'.format(question.id))
	else:
		form = AnswerForm(initial={'question' : question.id})

	return render(request, 'question.html', {'question': question,
											 'form': form,
											 'answers': question.answer_set.all(),})



def popular_questions(request):
	sorted_questions = Question.objects.order_by('-rating')
	paginator = Paginator(sorted_questions, 10)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
	      	queryset = paginator.page(paginator.num_pages)

	context = {
	    'sorted_questions': queryset,
	 }
	return render(request,'popular.html', context)



@login_required(login_url='/login/')
def add_question(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		form._user = request.user
		if form.is_valid():
			form = form.save()
			return HttpResponseRedirect('/question/{}'.format(form))
	else:
		form = AskForm()
	return render(request,'ask.html', {'form': form })



#signup/logout

def user_signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'thanks.html')
	else:	
		form = SignupForm()
	return render(request, 'signup.html', {'form': form })

	


def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
	else:	
		form = LoginForm()
	return render(request, 'login.html', {'form': form })






