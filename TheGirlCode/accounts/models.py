# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)   # Linking with the default django user model
    progress = models.IntegerField(default=0)  # Progress of the user
    answer_1 = models.CharField(max_length=50)

    def __str__(self):  # Displays names on the admin site
        return self.user.username


def create_profile(sender, **kwargs):  # Linking default User to UserProfile
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


