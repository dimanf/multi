# -*- coding: utf-8 -*-
from django.contrib import admin
from catalog.models import StoreThing, StoreCategory, StoreThingImage

class StoreThingImageAdmin(admin.ModelAdmin):
	pass

class StoreThingImageInline(admin.StackedInline):
	model = StoreThingImage
	max_num=10
	extra=0

class StoreThingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_create')
    list_display_links = ('name',)
    search_fields = ('name', 'date_create')
    inlines = [StoreThingImageInline,]

class StoreCategoryAdmin(admin.ModelAdmin):
    """Класс админки для категорий"""
    list_display = ('id', 'name', 'date_create')
    list_display_links = ('name',)
    search_fields = ('name', 'date_create')
    ordering = ('-date_create',)

admin.site.register(StoreCategory, StoreCategoryAdmin)
admin.site.register(StoreThingImage, StoreThingImageAdmin)
admin.site.register(StoreThing, StoreThingAdmin)