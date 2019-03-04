# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    interests = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=u'User interests')

    photo = models.ImageField(
        blank=True,
        upload_to='images/user_pics',
        default='../static/img/images.png',
        verbose_name=u'User Photo')

    created_on = models.DateField(
        auto_now_add=True,
        verbose_name=u'User Registration Date')

    def get_all_authors(self):
        return CustomUser.objects.all()[::-1]

    def get_current_user(self, request):
        return User.objects.get(pk=request.user.pk)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.user.username, self.user.first_name, self.user.last_name, self.user.email)
