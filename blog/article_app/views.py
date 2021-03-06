from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, View
#from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from blog.util import get_read_selected_category, get_read_selected_author#, get_selected_articles
from article_app.forms import CreateArticleForm
from article_app.models import Article, Category
from home_app.permissions import NeedLogin
from user_app.models import CustomUser


class Articles(View):

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

        return render(request, 'article_app/article.html', {
            'authors': authors, 'categories': categories, 'articles': articles})



class CreateArticleView(NeedLogin, View):
	"""CBV for writing new article"""

	model = Article
	form_class = CreateArticleForm
	template_name = 'article_app/create_article.html'

	def get(self, request, *args, **kwargs):
		form = CreateArticleForm()
		categories = Category.get_all_categories(self)
		return render(request, 'article_app/create_article.html', {'form': form, 'categories': categories})

	def post(self, request, *args, **kwargs):
		form = CreateArticleForm(data=request.POST)

		if form.is_valid():

			new_article = form.save(commit=False)
			new_article.author = CustomUser.get_current_user(self, request)
			new_article.save()
			return HttpResponseRedirect('%s?status_message=%s' %(reverse('article_app:create_url'), 'New article added!'))


class ReadArticleView(TemplateView):

	def get(self, request, *args, **kwargs):
		#selected_art_info = get_selected_articles(request)
		# selected_article = Article.objects.filter(title=selected_art_info.title)
		pk = request.COOKIES.get('selected_article_read')
		selected_article = Article.get_selected_articles_by_pk(self, pk)
		
		return render(request, 'article_app/read_article.html', {'selected_article': selected_article})


class EditArticleView(NeedLogin, UpdateView):
	model = Article
	form_class = CreateArticleForm
	#fields = ['title', 'content', 'category']
	template_name = 'article_app/edit_article.html'

	def get_success_url(self):
		return '%s?status_message=Article Edited!' %(reverse('article_app:read_article_url'))

	def post(self, request, *args, **kwargs):
		return super(EditArticleView, self).post(request, *args, **kwargs)

	# @method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(EditArticleView, self).dispatch(*args, **kwargs)


class DeleteArticleView(NeedLogin, DeleteView):
	model = Article
	template_name = 'article_app/delete_article.html'

	def get_success_url(self):
		return '%s?status_message=Article Deleted!' %(reverse('home_app:home_url'))

	def post(self, request, *args, **kwargs):
		return super(DeleteArticleView, self).post(request, *args, **kwargs)

	# @method_decorator(login_required)
	# def dispatch(self, *args, **kwargs):
	# 	return super(DeleteArticleView, self).dispatch(*args, **kwargs)

