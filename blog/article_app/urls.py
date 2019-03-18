from django.urls import path, include

from article_app.views import Articles, CreateArticleView, DeleteArticleView, EditArticleView, ReadArticleView

app_name = 'article_app'

urlpatterns = [
    path('', include([
   	    path('articles/', Articles.as_view(), name='articles_url'),
        path('create/', CreateArticleView.as_view(), name='create_url'),
        path('read/', ReadArticleView.as_view(), name='read_article_url'),
        path('edit/<int:pk>', EditArticleView.as_view(), name='edit_article_url'),
        path('delete/<int:pk>', DeleteArticleView.as_view(), name='delete_article_url'),
    ]))
]