# -*- coding: utf-8 -*-
from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from tinymce.models import HTMLField


class StoreCategory(models.Model):
    """Класс для категорий"""
    name = models.CharField(u'название категории', max_length=30)
    date_create = models.DateTimeField(u'дата создания', auto_now_add=True)

    def __unicode__(self):
        return self.name

    def get_thing_count(self):
        return self.storething_set.filter(approved=True).count()

    # def get_request_count(self):
    #     return self.storerequest_set.filter(approved=True).count()

    def get_all_objects(self):
        return self.objects.all()

    class Meta:
        verbose_name = u'категория'
        verbose_name_plural = u'категории'


class StoreThing(models.Model):
    """Класс для вещей"""
    name = models.CharField(u'название вещи', max_length=30)
    desc = HTMLField(u'описание')
    price = models.FloatField(u'Цена')
    date_create = models.DateTimeField(u'дата создания', auto_now_add=True)
    category = models.ForeignKey(StoreCategory, verbose_name = u'категория')
    approved = models.BooleanField(u'одобрено', help_text=u'Если отмечено, выводится на сайте')
    count = models.IntegerField(u'Кол-во')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'вещь'
        verbose_name_plural = u'вещи'

    def get_image(self):
        return self.storethingimage_set.get(thing_id=self.id)

# image = ImageWithThumbsField(u'изображение', upload_to='upload/images', blank=True, sizes=((200,200),(800,600)))

class StoreThingImage(models.Model):
    """Класс для изображений"""
    image = ImageWithThumbsField(u'изображение', upload_to='upload/images', blank=True, sizes=((200,200),(800,600)))
    thing = models.ForeignKey(StoreThing, verbose_name=u'вещь')
    date_create = models.DateTimeField(u'дата создания', auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.image

    class Meta:
        verbose_name = u'изображение'
        verbose_name_plural = u'изображения'