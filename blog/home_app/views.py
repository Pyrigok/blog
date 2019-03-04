from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

from blog.util import get_read_selected_category, get_read_selected_author, get_selected_articles
from article_app.models import Article, Category
from user_app.models import CustomUser


class Home(View):

    def get(self, request):
        read_category = get_read_selected_category(request)
        read_author = get_read_selected_author(request)

        authors = User.objects.all()
        #authors = CustomUser.get_all_authors(self)
        categories = Category.get_all_categories(self)

        if read_category:
            articles = Article.get_articles_filtered_by_category(self, read_category)[::-1]
        elif read_author:
            articles = Article.get_articles_filtered_by_author(self, read_author)[::-1]
        else:
            articles = Article.get_all_articles(self)[::-1]

        return render(request, 'home_app/home.html', {
            'authors': authors, 'categories': categories, 'articles': articles})
