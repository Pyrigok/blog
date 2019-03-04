# get selected category id from cookie for creating new article
def get_create_selected_category(request):

    pk = request.COOKIES.get('selected_category_create')

    if pk:
        from article_app.models.category_models import Category
        try:
            category_create = Category.objects.get(pk=int(pk))

        except Category.DoesNotExist:
            return None
        else:
            return category_create
    else:
        return None


# get selected category id from cookie for filtering articles
def get_read_selected_category(request):

    pk = request.COOKIES.get('selected_category_read')

    if pk:
        from article_app.models.category_models import Category
        try:
            category_read = Category.objects.get(pk=int(pk))

        except Category.DoesNotExist:
            return None
        else:
            return category_read
    else:
        return None


# get selected author's id from cookie for filtering articles
def get_read_selected_author(request):

    pk = request.COOKIES.get('selected_author_read')

    if pk:
        from user_app.models import CustomUser
        from django.contrib.auth.models import User
        try:
            selected_author_read = User.objects.get(pk=int(pk))

        except User.DoesNotExist:
            return None
        else:
            return selected_author_read
    else:
        return None


# get selected article's id for reading selected articles in a new page
def get_selected_articles(request):

    pk = request.COOKIES.get('selected_article_read')

    if pk:
        from article_app.models.article_models import Article
        try:
            selected_article = Article.objects.get(pk=int(pk))

        except Article.DoesNotExist:
            return None
        else:
            return selected_article
    else:
        return None
