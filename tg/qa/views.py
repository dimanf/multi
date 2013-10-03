# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
# from django.core.mail import send_mail
# from django.contrib.auth import logout


from qa.forms import qaform
from qa.models import qamodel
from news.models import News

def qa(request):

	if request.method == 'POST':
		form = qaform(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			q_a = qamodel(name = cd['name'],
				     email = cd['email'],
				     text = cd['text'])
			q_a.save()
			return HttpResponseRedirect('%s' % request.path)
	else:
		form = qaform()

	quest_answ = qamodel.objects.filter(status = 'public')


	return render(request, 'qa/qa.html',{
		'quest_answ': quest_answ,
		'form': form,
		})