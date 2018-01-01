# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from accounts.forms import *
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
            ans1 = form.cleaned_data['answer_1_1']
            ans2 = form.cleaned_data['answer_1_2']
            ans3 = form.cleaned_data['answer_1_3']
            ans4 = form.cleaned_data['answer_1_4']

            if ans1 == "Hello World" and profile.answer_1_1_check == False:
                profile.progress += 10
                profile.answer_1_1_check = True
                profile.save()
            form.save()

            if ans2 == 2 and profile.answer_1_2_check == False:
                profile.progress += 10
                profile.answer_1_2_check = True
                profile.save()
            form.save()

            if ans3 == "True" and profile.answer_1_3_check == False:
                profile.progress += 10
                profile.answer_1_3_check = True
                profile.save()
            form.save()

            if ans4 == 1500 and profile.answer_1_4_check == False:
                profile.progress += 10
                profile.answer_1_4_check = True
                profile.save()
            form.save()

        args = {'user': profile, 'form': form, }

        return render(request, 'accounts/course/course_1.html', args)

    else:
        form = CourseForm1(instance=profile)

        args = {'user': profile, 'form': form}
        return render(request, 'accounts/course/course_1.html', args)


def course_2(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = CourseForm2(request.POST, instance=profile)
        if form.is_valid():
            ans5 = form.cleaned_data['answer_2_1']
            ans6 = form.cleaned_data['answer_2_2']
            ans7 = form.cleaned_data['answer_2_3']
            ans8 = form.cleaned_data['answer_2_4']
            ans9 = form.cleaned_data['answer_2_5']

            if ans5 == "JamandButter" and profile.answer_2_1_check == False:
                profile.progress += 10
                profile.answer_2_1_check = True
                profile.save()
            form.save()

            if ans6 == "actor" and profile.answer_2_2_check == False:
                profile.progress += 10
                profile.answer_2_2_check = True
                profile.save()
            form.save()

            if ans7 == 24 and profile.answer_2_3_check == False:
                profile.progress += 10
                profile.answer_2_3_check = True
                profile.save()
            form.save()

            if ans8 == "lang[1]" and profile.answer_2_4_check == False:
                profile.progress += 10
                profile.answer_2_4_check = True
                profile.save()
            form.save()

            if ans9 == "Hop" and profile.answer_2_5_check == False:
                profile.progress += 10
                profile.answer_2_5_check = True
                profile.save()
            form.save()

        args = {'user': profile, 'form': form, }

        return render(request, 'accounts/course/course_2.html', args)

    else:
        form = CourseForm2(instance=profile)

        args = {'user': profile, 'form': form}
        return render(request, 'accounts/course/course_2.html', args)


def course_3(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = CourseForm3(request.POST, instance=profile)
        if form.is_valid():
            ans10 = form.cleaned_data['answer_3_1']
            ans11 = form.cleaned_data['answer_3_2']

            if ans10 == "Your party was a success!" and profile.answer_3_1_check == False:
                profile.progress += 10
                profile.answer_3_1_check = True
                profile.save()
            form.save()

            if ans11 == "You are ancient." and profile.answer_3_2_check == False:
                profile.progress += 10
                profile.answer_3_2_check = True
                profile.save()
            form.save()

        args = {'user': profile, 'form': form, }

        return render(request, 'accounts/course/course_3.html', args)

    else:
        form = CourseForm3(instance=profile)

        args = {'user': profile, 'form': form}
        return render(request, 'accounts/course/course_3.html', args)


def course_4(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = CourseForm4(request.POST, instance=profile)
        if form.is_valid():
            ans12 = form.cleaned_data['answer_4_1']
            ans13 = form.cleaned_data['answer_4_2']
            ans14 = form.cleaned_data['answer_4_3']

            if ans12 == 10 and profile.answer_4_1_check == False:
                profile.progress += 10
                profile.answer_4_1_check = True
                profile.save()
            form.save()

            if ans13 == "1 2 3" and profile.answer_4_2_check == False:
                profile.progress += 10
                profile.answer_4_2_check = True
                profile.save()
            form.save()

            if ans14 == "odd even odd even" and profile.answer_4_3_check == False:
                profile.progress += 10
                profile.answer_4_3_check = True
                profile.save()
            form.save()

        args = {'user': profile, 'form': form, }

        return render(request, 'accounts/course/course_4.html', args)

    else:
        form = CourseForm4(instance=profile)

        args = {'user': profile, 'form': form}
        return render(request, 'accounts/course/course_4.html', args)


def course_5(request):
    return render(request, 'accounts/course/course_5.html')


def course_6(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = CourseForm6(request.POST, instance=profile)
        if form.is_valid():
            ans15 = form.cleaned_data['answer_6_1']
            ans16 = form.cleaned_data['answer_6_2']
            ans17 = form.cleaned_data['answer_6_3']

            if ans15 == "butter" and profile.answer_6_1_check == False:
                profile.progress += 10
                profile.answer_6_1_check = True
                profile.save()
            form.save()

            if ans16 == "toffees chocolate" and profile.answer_6_2_check == False:
                profile.progress += 10
                profile.answer_6_2_check = True
                profile.save()
            form.save()

            if ans17 == "shopping_list.insert(2,\"juice\")" and profile.answer_6_3_check == False:
                profile.progress += 10
                profile.answer_6_3_check = True
                profile.save()
            form.save()

        args = {'user': profile, 'form': form, }

        return render(request, 'accounts/course/course_6.html', args)

    else:
        form = CourseForm6(instance=profile)

        args = {'user': profile, 'form': form}
        return render(request, 'accounts/course/course_6.html', args)


def course_7(request):
    return render(request, 'accounts/course/course_7.html')


def calc(request):
    return render(request, 'accounts/mini_projects/calculator.html')


def rps(request):
    return render(request, 'accounts/mini_projects/rps.html')


def pyglatin(request):
    return render(request, 'accounts/mini_projects/pyglatin.html')

