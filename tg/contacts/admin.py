# -*- coding: utf-8 -*-
from django.contrib import admin
from contacts.models import Burenie

class BurenieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'main_text', 'rigth_block_text')
    list_display_links = 'title',
    search_fields = ('title', 'main_text', 'rigth_block_text',)

admin.site.register(Burenie, BurenieAdmin) 