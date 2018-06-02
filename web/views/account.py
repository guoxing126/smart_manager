from django.shortcuts import render, redirect, HttpResponse
from repository import models
from utils.pagination import Pagination
from django.urls import reverse


def register(request, *args, **kwargs):


    return render(request,'register.html')


def login(request, *args, **kwargs):
    pass


def loginout(request, *args, **kwargs):
    pass
