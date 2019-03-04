from django.urls import path, include

from article_app.views import CreateArticleView, DeleteArticleView, EditArticleView, ReadArticleView

app_name = 'article_app'

urlpatterns = [
    path('articles/', include([
        path('', CreateArticleView.as_view(), name='create_url'),
        path('read/', ReadArticleView.as_view(), name='read_article_url'),
        path('edit/<int:pk>', EditArticleView.as_view(), name='edit_article_url'),
        path('delete/<int:pk>', DeleteArticleView.as_view(), name='delete_article_url'),
    ]))
]