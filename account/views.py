from django import http
from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.html import escape
from .forms import LoginForm, UserRegistrationForm, ProfileEditForm, UserEditForm

from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

# Login
# def user_login(request):
    # if request.method == "POST":
    #     form = LoginForm(request, user)
    #     if form.is_valid():
    #         user = authenticate(
    #             request,
    #             username=['username'],
    #             password=['password']
    #         )

    #         if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #                 return render('home')

    #             else:
    #                 return HttpResponse('Disabled login')
            
    #         else:
    #             return HttpResponse('Check your email and password')
    # else:
    # #     form = LoginForm()
    # return render(request, 'accounts/login.html')
# 'Your account has been created. Now you can log in' messages.success(request, 'Your account has been created. Now you can log in')
# Register
def register(request):

    if request.method == "POST":

        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create new user obj
            new_user = user_form.save(commit=False)
            # set the password
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            # save the obj
            new_user.save()
            Profile.objects.create(user=new_user)
            messages.success(request, 'Your account has been created. Now you can log in')
            return render(request,'registration\login.html', {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})

# Edit Profile
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
        data=request.POST,
        files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
    
    
    return render(request,'accounts/edit.html',{'user_form': user_form,'profile_form': profile_form})
