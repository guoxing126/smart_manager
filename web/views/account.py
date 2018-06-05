from django.shortcuts import render, redirect, HttpResponse
from repository import models
from utils.pagination import Pagination
from django.urls import reverse
from web.forms.account import RegisterForm, LoginForm


def register(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        reg_form = RegisterForm(request=request, data=request.POST)
        if reg_form.is_valid():
            models.UserInfo.objects.create(
                username=reg_form.cleaned_data['username'],
                password=reg_form.cleaned_data['password'],
                nickname=reg_form.cleaned_data['nickname'],
                email=reg_form.cleaned_data['email']
            )
            return redirect('/')
        else:
            return render(request, 'register.html', {'reg_form': reg_form})


def login(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        log_form = LoginForm(request=request, data=request.POST)
        if log_form.is_valid():
            username = log_form.cleaned_data.get('username')
            password = log_form.cleaned_data.get('password')
            user_info = models.UserInfo.objects.filter(username=username, password=password). \
                values('nid', 'nickname',
                       'username', 'email',
                       'avatar',
                       'blog__nid',
                       'blog__site').first()
            request.session['user_info'] = user_info
            # if form.cleaned_data.get('rmb'):
            #     request.session.set_expiry(60 * 60 * 24 * 30)
            return redirect('/')
        else:
            print(log_form.errors)
            return render(request, 'login.html', {'log_form': log_form})


def loginout(request, *args, **kwargs):
    request.session.clear()
    print(request.session)
    return redirect('/')
