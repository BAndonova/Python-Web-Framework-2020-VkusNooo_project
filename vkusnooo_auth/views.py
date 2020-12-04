from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from vkusnooo_auth.forms import RegisterForm


def register_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm()
        }
        return render(request, 'auth/register.html', context)
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

        context = {
            'form': form
        }
        return render(request, 'auth/register.html', context)


def login_view(request):
    username = 'bibsand'
    password = 'qwe!@#'
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect('index')
    return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')
