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
    url(r'^network_list.html', home.network_list),
    url(r'^server_list.html',home.server_list),
    url(r'^device_manage.html',home.device_manage),
    url(r'^device_alert.html',home.device_alert),
    url(r'^system_settings.html',home.system_settings),
    url(r'^', home.device_overview),
]
