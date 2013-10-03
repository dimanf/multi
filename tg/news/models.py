# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
    """docstring for News"""
    title = models.CharField(u'Название новости', max_length=30)
    text = HTMLField(u'Текст новости')
    date_create = models.DateTimeField(u'Дата создания', auto_now=True)

    def __unicode__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return "/news/%i/" % self.id

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        # app_label = u'Новости'

