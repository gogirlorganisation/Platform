# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   # Linking with the default django user model
    progress = models.IntegerField(default=0)  # Progress of the user

    answer_1_1 = models.CharField(max_length=50,default="")
    answer_1_1_check = models.BooleanField(default=False)

    answer_1_2 = models.IntegerField(default=0)
    answer_1_2_check = models.BooleanField(default=False)

    answer_1_3 = models.CharField(max_length=50,default="")
    answer_1_3_check = models.BooleanField(default=False)

    answer_1_4 = models.IntegerField(default=0)
    answer_1_4_check = models.BooleanField(default=False)

    answer_2_1 = models.CharField(max_length=50,default="")
    answer_2_1_check = models.BooleanField(default=False)

    answer_2_2= models.CharField(max_length=50,default="")
    answer_2_2_check = models.BooleanField(default=False)

    answer_2_3 = models.IntegerField(default=0)
    answer_2_3_check = models.BooleanField(default=False)

    answer_2_4 = models.CharField(max_length=50,default="")
    answer_2_4_check = models.BooleanField(default=False)

    answer_2_5 = models.CharField(max_length=50,default="")
    answer_2_5_check = models.BooleanField(default=False)

    answer_3_1 = models.CharField(max_length=50, default="")
    answer_3_1_check = models.BooleanField(default=False)

    answer_3_2 = models.CharField(max_length=50, default="")
    answer_3_2_check = models.BooleanField(default=False)

    answer_4_1 = models.IntegerField(default=0)
    answer_4_1_check = models.BooleanField(default=False)

    answer_4_2 = models.CharField(max_length=50, default="")
    answer_4_2_check = models.BooleanField(default=False)

    answer_4_3 = models.CharField(max_length=50, default="")
    answer_4_3_check = models.BooleanField(default=False)

    answer_5_1 = models.CharField(max_length=50, default="")
    answer_5_1_check = models.BooleanField(default=False)

    answer_6_1 = models.CharField(max_length=50, default="")
    answer_6_1_check = models.BooleanField(default=False)

    answer_6_2 = models.CharField(max_length=50, default="")
    answer_6_2_check = models.BooleanField(default=False)

    answer_6_3 = models.CharField(max_length=50, default="")
    answer_6_3_check = models.BooleanField(default=False)

    answer_7_1 = models.CharField(max_length=50, default="")
    answer_7_1_check = models.BooleanField(default=False)

    answer_7_2 = models.IntegerField(default=0)
    answer_7_2_check = models.BooleanField(default=False)

    def __str__(self):  # Displays names on the admin site
        return self.user.username


def create_profile(sender, **kwargs):  # Linking default User to UserProfile
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


