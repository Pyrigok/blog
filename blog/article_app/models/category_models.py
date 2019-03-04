# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name = u'Article Category'
        verbose_name_plural = u'Article Categories'

    category_name = models.CharField(
        max_length=20,
        blank=False,
        verbose_name=u'Category Name')

    def get_all_categories(self):
        return Category.objects.all()

    def __str__(self):
        return '%s' % self.category_name
