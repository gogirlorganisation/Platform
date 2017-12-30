# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from accounts.forms import RegistrationForm, EditProfileForm, CourseForm1
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def login(request):

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':  # when submit button is clicked with the user details
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))

    else:  # GET method, i.e. user is requesting the page
        form = RegistrationForm()

    return render(request, 'accounts/sign_up.html', {'form': form})


@login_required  # Page becomes inaccessible to users which are not logged in
def view_profile(request):

    return render(request, 'accounts/profile.html', {'user': request.user})


@login_required
def edit_profile(request):

    if request.method == 'POST':  # When user is submitting the updated info
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:profile'))

    else:  # When the user wants to view the page
        form = EditProfileForm(instance=request.user)

        return render(request, 'accounts/editprofile.html', {'form': form})
    

@login_required
def change_password(request):

    if request.method == 'POST':  # When user is submitting the updated info
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Doesn't logout the user after pw change
            return redirect(reverse('accounts:profile'))

        else:  # If form is not valid, redirects to the same page
            return redirect(reverse('accounts:change_password'))

    else:
        form = PasswordChangeForm(user=request.user)

        return render(request, 'accounts/changepassword.html', {'form': form})


def compiler(request):
    return render(request, 'accounts/compiler.html')


@login_required
def course_1(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = CourseForm1(request.POST, instance=profile)
        if form.is_valid():
            ans = form.cleaned_data['answer_1']

            if ans == "Hello World" and profile.answer_1_check == False:
                profile.progress += 10
                profile.answer_1_check = True
                profile.save()
            form.save()

        args = {'user': profile, 'form': form, 'ans':ans}

        return render(request, 'accounts/course/course_1.html', args)

    else:
        form = CourseForm1(instance=profile)

        args = {'user': profile, 'form': form}
        return render(request, 'accounts/course/course_1.html', args)


def course_2(request):
    return render(request, 'accounts/course/course_2.html')


def course_3(request):
    return render(request, 'accounts/course/course_3.html')


def course_4(request):
    return render(request, 'accounts/course/course_4.html')


def course_5(request):
    return render(request, 'accounts/course/course_5.html')


def course_6(request):
    return render(request, 'accounts/course/course_6.html')


def course_7(request):
    return render(request, 'accounts/course/course_7.html')


def course_8(request):
    return render(request, 'accounts/course/course_8.html')


def course_9(request):
    return render(request, 'accounts/course/course_9.html')

