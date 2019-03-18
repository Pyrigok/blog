# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, FormView, RedirectView, TemplateView, UpdateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from home_app.permissions import NeedLogin
from user_app.models import CustomUser
from user_app.forms import CustomUserCreationForm, LoginForm, UserForm


class AuthorListView(TemplateView):
    """CBV for author list"""

    def get(self, request, *args, **kwargs):
        authors = CustomUser.get_all_authors(self)
        return render(request, 'user_app/authors.html', {'authors': authors})


class LoginView(TemplateView):
    """CBV for Log In"""

    # form_class = LoginForm
    template_name = 'user_app/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/article/articles/')
        return render(request, 'user_app/login.html', {})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/article/articles/')
            return HttpResponse("Your account was inactive.")
        else:
            return HttpResponseRedirect('%s?status_message=%s' %(reverse('user_app:login_url'), 'This account does not exist!'))
            #return HttpResponse("Invalid login details given")


class LogoutView(NeedLogin, RedirectView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')


class SignUpView(View):
    # model = User
    # form_class = UserForm
    # template_name = 'user_app/signup.html'

    # def get_success_url(self):
    #     return HttpResponseRedirect((reverse('home_app:home_url')))

    # def post(self, request, *args, **kwargs):
    #     if request.POST.get('send_button'):
    #         return super(SignUpView, self).post(request, *args, **kwargs)

    #     else:
    #         return HttpResponseRedirect(reverse('home_app:home_url'))
    
    form = UserForm()

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/article/articles/')
        custom_form = CustomUserCreationForm()
        return render(request, 'user_app/signup.html', {'form': self.form, 'custom_form': custom_form})

    def post(self, request):
        self.form = UserForm(request.POST)
        custom_form = CustomUserCreationForm(data=request.POST)

        if self.form.is_valid():
            user = self.form.save()
            user.set_password(self.form.cleaned_data['password'])
            user.save()
            profile = custom_form.save(commit=False)
            profile.user = user
            profile.photo = request.FILES.get('photo')
            profile.save()
            return HttpResponseRedirect('/users/login/')

        return render(request, 'user_app/signup.html', {'error': self.form.non_field_errors(), 'form': self.form})


class UpdateUserView(NeedLogin, UpdateView):
    """CBV for update user info"""

    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'user_app/user_profile.html'
    success_url = '/article/articles/'