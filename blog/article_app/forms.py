from django import forms

from article_app.models.article_models import Article


class CreateArticleForm(forms.ModelForm):

	class Meta:
		model = Article
		fields = ('title', 'category', 'content')

	category = forms.Select()
	content = forms.CharField(max_length=2560, widget=forms.Textarea())
