# -*- coding: utf-8 -*-
from news.models import News
from django.views.generic import ListView, DetailView

class NewsListView(ListView):
	model = News

class NewsDetailView(DetailView):
	model = News