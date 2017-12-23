
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'TheGirlCode/landingpage.html')


def about_us(request):
    return render(request, 'TheGirlCode/aboutus.html')


def workshops(request):
    return render(request, 'TheGirlCode/workshops.html')