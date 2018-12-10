import json
import inspect

from django.shortcuts import render, redirect, HttpResponse
from repository import models
from utils.pagination import Pagination
from django.urls import reverse


def device_overview(request, *args, **kwargs):
    '''
    管理概况
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    side_name = inspect.stack()[0][3]
    context_data ={
        'side_name':side_name,
    }
    return render(request, 'home.html', context_data)


def network_list(request, *args, **kwargs):
    '''
    网络设备列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    side_name = inspect.stack()[0][3]
    context_data = {
        'side_name': side_name,
    }
    return render(request, 'network_list.html', context_data)


def server_list(request, *args, **kwargs):
    '''
    服务器列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    side_name = inspect.stack()[0][3]
    context_data = {
        'side_name': side_name,
    }
    return render(request, 'server_list.html', context_data)


def device_manage(request, *args, **kwargs):
    '''
    设备管理
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    side_name = inspect.stack()[0][3]
    context_data = {
        'side_name': side_name,
    }
    return render(request, 'device_manage.html', context_data)


def device_alert(request, *args, **kwargs):
    '''
    设备告警
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    side_name = inspect.stack()[0][3]
    context_data = {
        'side_name': side_name,
    }
    return render(request, 'device_alert.html', context_data)


def system_settings(request, *args, **kwargs):
    '''
    系统设置
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    side_name = inspect.stack()[0][3]
    context_data = {
        'side_name': side_name,
    }
    return render(request, 'system_settings.html', context_data)