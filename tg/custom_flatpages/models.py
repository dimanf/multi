# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm
from django.contrib.flatpages.models import FlatPage

from ckeditor.widgets import CKEditorWidget

class FlatpageForm(FlatpageForm):
    head = forms.CharField(widget=forms.Textarea)

class MyFlatPageAdmin(FlatPageAdmin):
    form = FlatpageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)