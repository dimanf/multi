# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from news.models import News

def menu_processor(request):
    path = request.path.split('/')[1]
    return {
        'path': path,
    }

def news_block(request):
    last_news = News.objects.all().order_by('-date_create')[:5]

    return {
        'last_news': last_news,
    }
