# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context

from orders.models import Orders
from orders.forms import OrderForm
from catalog.models import StoreThing

def to_order(request, product_id):
	thing = StoreThing.objects.get(id=product_id)

	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			order = Orders(
				name = cd['name'],
				s_name = cd['s_name'],
				p_name = cd['p_name'],
				address = cd['address'],
				phone = cd['phone'],
				email = cd['email'],
				product = thing,
				quantity = cd['quantity'],
				)

			order.save()

			send_mail(
				u'Поступил новый заказ',
				get_template('mail/store_thing_add.txt').render(
					Context({
						's_name': cd['s_name'],
						'name': cd['name'],
						'p_name': cd['p_name'],
						'address': cd['address'],
						'phone': cd['phone'],
						'email': cd['email'],
						'product': thing,
						'quantity': cd['quantity']
						})
					),
					'multivarka_skorovarka72@mail.ru',
					['multivarka_skorovarka72@mail.ru'])

			return HttpResponseRedirect('/thx/')

	else:
		form = OrderForm()

	return render(request, 'catalog/storething_detail.html', {
		'order_form': form,
		'thing': thing,
	})

def thx(request):
	return render(request, 'thx.html')


