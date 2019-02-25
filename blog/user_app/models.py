from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    interests = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=u'User interests')

    photo = models.ImageField(
        blank=True,
        default='../static/img/images.png',
        verbose_name=u'User Photo')


    created_on = models.DateField(
        auto_now_add=True,
        verbose_name=u'User Registration Date')

    def __str__(self):
        return '%s, %s' %(self.username, self,email)