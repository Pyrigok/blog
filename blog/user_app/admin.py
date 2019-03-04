from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

#from user_app.forms import CustomUserCreationForm, CustomUserChangeForm
from user_app.models import CustomUser

# class CustomUserAdmin(UserAdmin):
#    # add_form = CustomUserCreationForm
#    # form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['user']

admin.site.register(CustomUser)#, CustomUserAdmin)