# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from . import views

urlpatterns = [

    url(r'^$', views.home_page , name='index'),
    url(r'^login/.*$', views.user_login, name='login'),
    url(r'^signup/.*$', views.user_signup, name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', views.question_details, name='question'),
    url(r'^ask/.*$', views.add_question, name='ask'),
    url(r'^popular/.*$', views.popular_questions, name='popular'),
    #url(r'^new/.*$', 'qa.views.test', name='new'),
]
