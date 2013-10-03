# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from news.views import NewsListView, NewsDetailView
from news.models import News

urlpatterns = patterns('',
url(r'^$', NewsListView.as_view(queryset=News.objects.order_by('-date_create')), name='list'), # то есть по URL http://имя_сайта/blog/
                                               # будет выводиться список постов
url(r'^(?P<pk>\d+)/$', NewsDetailView.as_view()), # а по URL http://имя_сайта/blog/число/
                                              # будет выводиться пост с определенным номером

)
