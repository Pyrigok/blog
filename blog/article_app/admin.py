from django.contrib import admin

from article_app.models.article_models import Article
from article_app.models.category_models import Category

admin.site.register(Article)
admin.site.register(Category)