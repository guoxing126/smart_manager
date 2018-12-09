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
    return render(request, 'home.html')


def network_list(request, *args, **kwargs):
    '''
    网络设备列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    pass


def server_list(request, *args, **kwargs):
    '''
    服务器列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    pass


def device_manage(request, *args, **kwargs):
    '''
    设备管理
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    pass


def device_alert(request, *args, **kwargs):
    '''
    设备告警
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    pass


def system_settings(request, *args, **kwargs):
    '''
    系统设置
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    pass