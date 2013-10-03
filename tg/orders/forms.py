# -*- coding: utf-8 -*-
from django import forms

class OrderForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
	s_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
	p_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
	address = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Адрес'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email'}))
	quantity = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Количество'}))