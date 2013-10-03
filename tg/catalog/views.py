# -*- coding: utf-8 -*-
from catalog.models import StoreThing, StoreCategory
from django.views.generic import ListView, DetailView
from django.shortcuts import render
# from django.views.generic.list_detail import object_list

class StoreCategoryListView(ListView):
	model = StoreCategory
	queryset = StoreCategory.objects.all()

def StoreThingListView(request, cat_id):
	storething_list = StoreThing.objects.filter(category__id=cat_id).order_by('-date_create')
	return render(request, 'catalog/storething_list.html', {
		'storething_list': storething_list,
		})

def StoreThingDetailView(request, ting_id):
	q = ting_id
	item = StoreThing.objects.get(id=1)
	return render(request, 'catalog/storething_detail.html', {
		'item': item,
		'q': q,
		})



# # -*- coding: utf-8 -*-
# from catalog.models import StoreThing
# from django.views.generic import ListView, DetailView

# class StoreThingListView(ListView):
# 	model = StoreThing

# class StoreThingDetailView(DetailView):
# 	model = StoreThing
