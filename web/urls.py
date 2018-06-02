from django.conf.urls import url

from .views import home,account

urlpatterns = [
    url(r'^all/(?P<article_type_id>\d+).html',home.blog_index,name='index'),
    url(r'^home', home.blog_home),
    url(r'^filter', home.blog_filter),
    url(r'^detail', home.blog_detail),
    url(r'^login',account.login),
    url(r'^register',account.register),
    url(r'^loginout',account.loginout),
    url(r'^', home.blog_index,name='index'),
]