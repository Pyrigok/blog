from django.urls import path

from user_app.views import AuthorListView, LoginView, LogoutView, SignUpView

app_name = 'user_app'

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors_url'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('signup/', SignUpView.as_view(), name='signup_url'),

]