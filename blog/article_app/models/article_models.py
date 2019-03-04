# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from user_app.models import CustomUser
from article_app.models.category_models import Category


class Article(models.Model):

    class Meta:
        verbose_name = u'Article'
        verbose_name_plural = u'Articles'

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT)

    title = models.CharField(
        max_length=70,
        blank=False,
        verbose_name=u"Article title")

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        verbose_name=u'Article category')

    content = models.CharField(
        max_length=1000,
        blank=False,
        verbose_name=u'Article content')

    created_on = models.DateField(
        auto_now_add=True,
        verbose_name=u'Date of add of Article')

    def get_articles_filtered_by_category(self, read_category):
        try:
            articles = Article.objects.filter(category=read_category)
        except Article.DoesNotExist:
            articles = None
        return articles

    def get_articles_filtered_by_author(self, read_author):
        try:
            articles = Article.objects.filter(author=read_author)
        except Article.DoesNotExist:
            articles = None
        return articles

    def get_selected_articles_by_pk(self, pk):
        try:
            articles = Article.objects.filter(pk=pk)
        except Article.DoesNotExist:
            articles = None
        return articles

    def get_all_articles(self):
        return Article.objects.all()

    def __str__(self):
        return '%s %s %s %s %s' % (self.author, self.title, self.category, self.content, self.created_on)
