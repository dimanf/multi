# -*- coding: utf-8 -*-
from django.contrib import admin
from orders.models import Orders

class OrdersAdmin(admin.ModelAdmin):
	list_display = ('id', 's_name', 'name', 'p_name', 'phone', 'email', 'date_create')
	list_display_links = ('name',)
	search_fields = ('s_name', 'name', 'p_name', 'phone', 'email', 'date_create')
	ordering = ('-date_create',)

admin.site.register(Orders, OrdersAdmin)