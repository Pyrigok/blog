from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user_app.models import CustomUser


class CustomUserCreationForm(UserCreationForm):


    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'interests', 'photo')

class CustomUserChangeForm(UserChangeForm):


    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'interests', 'photo')