# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.decorators.http import require_GET, require_POST

from .models import Question, Answer
#from .forms import AskForm, AnswerForm, SignupForm, LoginForm


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def test(request, *args, **kwargs):
	return HttpResponse('OK')

def home_page(request):
	questions=Question.objects.order_by('-id')
	paginator=Paginator(questions,10)
	page=request.GET.get('page',1)
	try:
		queryset=paginator.page(page)
	except PageNotAnInteger:
		queryset =paginator.page(1)
	except EmptyPage:
		queryset=paginator.page(paginator.num_pages)
	context={'questions':queryset,
			 }
	return render(request,'index.html',context)