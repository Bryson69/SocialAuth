from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        form  = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('home')
                else:
                    return HttpResponse("Disabled Account")
            else:
                return HttpResponse("Check the information you put in again")
        
    else:
        form = LoginForm()
            
    return render(request, 'accounts/login.html', {'form': form})