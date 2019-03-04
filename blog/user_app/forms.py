from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

from user_app.models import CustomUser


class UserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

        password = forms.CharField(widget=forms.PasswordInput())
        email = forms.EmailField(widget=forms.EmailInput())


class CustomUserCreationForm(forms.ModelForm):

    class Meta():
        model = CustomUser
        fields = ('interests', 'photo')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
