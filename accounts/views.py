from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        return redirect('home')
    return render(request, 'accounts/form.html', {'form':form, 'title':'Giris YAP'})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.email=form.cleaned_data.get('e_mail')
        user.first_name=form.cleaned_data.get('first_name')
        user.last_name=form.cleaned_data.get('last_name')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,password=password)
        login(request,new_user)
        return redirect('home')
    return render(request, 'accounts/form.html', {'form':form, 'title':'Uye OL'})


def logout_view(request):
    logout(request)
    return redirect('home')
