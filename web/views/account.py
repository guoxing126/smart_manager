from django.shortcuts import render, redirect, HttpResponse
from repository import models
from utils.pagination import Pagination
from django.urls import reverse
from web.forms.account import RegisterForm,LoginForm


def register(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        post_data = request.POST
        print(post_data)
        reg_form = RegisterForm(request=request,data=request.POST)
        if reg_form.is_valid():
            print('clean_data',reg_form.cleaned_data)
            return redirect('/')
        else:
            print('errors',reg_form.errors)
            return render(request,'register.html',{'reg_form':reg_form})


def login(request, *args, **kwargs):
    pass


def loginout(request, *args, **kwargs):
    pass
