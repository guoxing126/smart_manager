from django.conf.urls import url

from .views import home, account

urlpatterns = [
    # url(r'^all/(?P<article_type_id>\d+).html', home.blog_index, name='index'),
    # url(r'^check_code.html', account.check_code),
    url(r'^login.html', account.login),
    url(r'^register.html', account.register),
    url(r'^logout.html', account.logout),
    # url(r'^index.html', home.blog_index, name='index'),
    url(r'^home.html',home.device_overview),
    url(r'^', home.device_overview),
]
