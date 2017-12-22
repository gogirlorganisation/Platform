# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import UserProfile

admin.site.register(UserProfile)
admin.site.site_header = "The Girl Code Administration"