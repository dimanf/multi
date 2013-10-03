# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from tg.news.models import News

def last_news(request):

    last_news = News.objects.all()[:10]

    return render_to_response('base.html', locals(),\
    context_instance = RequestContext(request))
