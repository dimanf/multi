# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from catalog.models import StoreThing, StoreCategory
from catalog.views import StoreThingListView, StoreThingDetailView, StoreCategoryListView
from orders.views import to_order

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', StoreCategoryListView.as_view(), name='category'),
	url(r'^(\w+)/$', StoreThingListView, name='thing'),
	url(r'^item/(\d+)/$', to_order),
)


# # -*- coding: utf-8 -*-
# from django.conf.urls import patterns, include, url
# from django.contrib import admin

# from catalog.models import StoreThing
# from catalog.views import StoreThingListView, StoreThingDetailView

# admin.autodiscover()

# urlpatterns = patterns('',
# 	url(r'^$', StoreThingListView.as_view(queryset=StoreThing.objects.filter(approved=True).order_by('-date_create')), name='thing'),
# 	# url(r'^(?P<pk>\d+)/$', StoreThingDetailView.as_view()),
# 	# url(r'^(?P<pk>\d+)/$', to_order),
# )