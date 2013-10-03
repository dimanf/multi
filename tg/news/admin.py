# -*- coding: utf-8 -*-
from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    """Класс админки для новостей"""
    list_display = ('title', 'date_create')
    list_display_links = ('title',)
    search_fields = ('title', 'date_create')

admin.site.register(News, NewsAdmin)
