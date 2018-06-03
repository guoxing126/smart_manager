from django.shortcuts import render, redirect, HttpResponse
from repository import models
from utils.pagination import Pagination
from django.urls import reverse


def blog_index(request, *args, **kwargs):
    if kwargs:
        article_type_id = int(kwargs['article_type_id'])
        base_url = reverse('index',kwargs=kwargs)
    else:
        article_type_id = None
        base_url = '/'

    data_count = models.Article.objects.filter(**kwargs).count()
    page_obj = Pagination(request.GET.get('p'),data_count=data_count)

    article_list = models.Article.objects.filter(**kwargs)[page_obj.start:page_obj.end]
    article_type_list = models.Article.type_choices

    page_str = page_obj.page_str(base_url)
    context_data = {
        'article_list':article_list,
        'article_type_list':article_type_list,
        'article_type_id':article_type_id,
        'page_obj':page_obj,
        'page_str':page_str,
    }

    return render(request,'index.html', context_data)


def blog_home(request, *args, **kwargs):
    pass


def blog_filter(request, *args, **kwargs):
    pass


def blog_detail(request, *args, **kwargs):
    pass
