import json
import inspect

from django.shortcuts import render, redirect, HttpResponse
from repository import models
from utils.pagination import Pagination
from django.urls import reverse

sidebar_dcit = {
    'device_overview':'管理概况',
    'network_list':'网络设备列表',
    'server_list': '服务器列表',
    'device_manage': '设备管理',
    'device_alert': '设备告警',
    'system_settings': '系统设置',
}


def device_overview(request, *args, **kwargs):
    '''
    管理概况
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    fname = inspect.stack()[0][3]
    sidebar_name = sidebar_dcit.get(fname)
    context_data ={
        'fname':fname,
        'sidebar_name':sidebar_name,
        'sidebar_dcit':sidebar_dcit,
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
    fname = inspect.stack()[0][3]
    sidebar_name = sidebar_dcit.get(fname)
    context_data = {
        'fname': fname,
        'sidebar_name': sidebar_name,
        'sidebar_dcit': sidebar_dcit,
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
    fname = inspect.stack()[0][3]
    sidebar_name = sidebar_dcit.get(fname)
    context_data = {
        'fname': fname,
        'sidebar_name': sidebar_name,
        'sidebar_dcit': sidebar_dcit,
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
    fname = inspect.stack()[0][3]
    sidebar_name = sidebar_dcit.get(fname)
    context_data = {
        'fname': fname,
        'sidebar_name': sidebar_name,
        'sidebar_dcit': sidebar_dcit,
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
    fname = inspect.stack()[0][3]
    sidebar_name = sidebar_dcit.get(fname)
    context_data = {
        'fname': fname,
        'sidebar_name': sidebar_name,
        'sidebar_dcit': sidebar_dcit,
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
    fname = inspect.stack()[0][3]
    sidebar_name = sidebar_dcit.get(fname)
    context_data = {
        'fname': fname,
        'sidebar_name': sidebar_name,
        'sidebar_dcit': sidebar_dcit,
    }
    return render(request, 'system_settings.html', context_data)