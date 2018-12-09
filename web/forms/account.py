from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django import forms as django_forms
from django.forms import fields as django_fields
from django.forms import widgets as django_widgets
from repository import models


class BaseForm(object):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(BaseForm, self).__init__(*args, **kwargs)


class LoginForm(BaseForm, django_forms.Form):
    username = django_fields.CharField()
    password = django_fields.CharField()

    # def clean_username(self):
    #     post_username = self.cleaned_data['username']
    #     if not models.UserInfo.objects.filter(username=post_username).exists():
    #         raise ValidationError('用户名不存在')
    #     return post_username

    def clean_password(self):
        post_username = self.cleaned_data['username']
        post_password = self.cleaned_data['password']
        if not models.UserInfo.objects.filter(username=post_username,password=post_password).exists():
            raise ValidationError('用户名或密码错误')
        return post_password

    # rmb = django_fields.IntegerField(required=False)
    # check_code = django_fields.CharField(
    #     error_messages={'required': '验证码不能为空.'}
    # )

    # def clean_check_code(self):
    #     if self.request.session.get('CheckCode').upper() != self.request.POST.get('check_code').upper():
    #         raise ValidationError(message='验证码错误', code='invalid')


class RegisterForm(BaseForm, django_forms.Form):
    username = django_fields.CharField(
        min_length=6,
        max_length=20,
        required=True,
        error_messages={'required': '用户名不能为空.', 'min_length': "用户名长度不能小于6个字符", 'max_length': "用户名长度不能大于32个字符"}
    )
    password = django_fields.RegexField(
        '^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$\%\^\&\*\(\)])[0-9a-zA-Z!@#$\%\^\&\*\(\)]{8,32}$',
        min_length=8,
        max_length=32,
        required=True,
        error_messages={'required': '密码不能为空.',
                        'invalid': '密码必须包含数字，字母、特殊字符',
                        'min_length': "密码长度不能小于8个字符",
                        'max_length': "密码长度不能大于32个字符"}
    )
    confirm_password = django_fields.RegexField(
        '^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$\%\^\&\*\(\)])[0-9a-zA-Z!@#$\%\^\&\*\(\)]{8,32}$',
        min_length=8,
        max_length=32,
        required=True,
        error_messages={'required': '密码不能为空.',
                        'invalid': '密码必须包含数字，字母、特殊字符',
                        'min_length': "密码长度不能小于8个字符",
                        'max_length': "密码长度不能大于32个字符"}
    )

    def clean_username(self):
        post_username = self.cleaned_data['username']
        if models.UserInfo.objects.filter(username=post_username).exists():
            raise ValidationError('用户已注册')
        return post_username

    def clean(self):
        v1 = self.cleaned_data.get('password')
        v2 = self.cleaned_data.get('confirm_password')
        if v1 == v2:
            return self.cleaned_data
        else:
            raise ValidationError('密码输入不一致')
