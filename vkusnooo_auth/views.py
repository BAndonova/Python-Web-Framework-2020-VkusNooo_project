from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
# from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from vkusnooo_auth.forms import RegisterForm, ProfileForm, LoginForm


def get_redirect_url(params):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else 'index'


@transaction.atomic
def register_user(request):
    if request.method == 'GET':

        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'auth/register.html', context)
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        return_url = get_redirect_url(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect(return_url)

        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'auth/register.html', context)


def login_user(request):
    if request.method == "GET":
        context = {
            'login_form': LoginForm(),
        }
        return render(request, 'auth/login.html', context)

    else:
        login_form = LoginForm(request.POST)

        return_url = get_redirect_url(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(return_url)

        context = {
            'login_form': LoginForm(),
        }
        return render(request, 'auth/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('index')


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    profile = user.userprofile
    if request.method == 'GET':
        context ={
            'profile_user': user,
            'profile': profile,
            'recipes': user.recipe_set.all(),
            'form': ProfileForm(),
        }
        return render(request, 'auth/user_profile.html', context)
    else:
        form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')

        return redirect('current user profile')
