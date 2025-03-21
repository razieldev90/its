from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def home(request):
    return render(request, 'prog_accounts/home.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in...')
                return redirect('home')
            else:
                messages.error(
                    request, 'Incorrect username or password... Try again...')

    ctx = {
        'form': form,
    }

    return render(request, 'prog_accounts/login.html', ctx)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered...')
            return redirect('home')

    ctx = {
        'form': form,
    }
    return render(request, 'prog_accounts/register.html', ctx)


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out...')
    return redirect('home')
