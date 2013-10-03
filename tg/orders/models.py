# -*- coding: utf-8 -*-
from django.db import models

class Orders(models.Model):
	name = models.CharField(u'Имя', max_length=40)
	s_name = models.CharField(u'Фамилия', max_length=50)
	p_name = models.CharField(u'Отчество', max_length=50)
	address = models.TextField(u'Адрес')
	phone = models.CharField(u'Телефон', max_length=11)
	email = models.EmailField()
	product = models.CharField(u'Название товара', max_length=40)
	quantity = models.IntegerField(u'Количество товара')
	date_create = models.DateTimeField(u'дата заказа', auto_now_add=True)

	def __unicode__(self):
		return '%s %s. %s.' % (self.s_name, self.name, self.p_name)

	class Meta:
		verbose_name = u'Заказ'
		verbose_name_plural = u'Заказы'
