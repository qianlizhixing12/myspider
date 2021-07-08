from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.apps import apps
from django.db.models import Count
from django.shortcuts import render
from api.tool import user_to_response
from .models import AuthUser, AuthUserAttrDefine, ScrapyUpdateInfo


def server_error(request):
    return render(request, '500.html')


def forbidden(request, exception):
    return render(request, '403.html')


def page_not_found(request, exception):
    return render(request, '404.html')


def loginpage(request):
    return render(request, 'login.html')


@login_required
def indexpage(request):
    page_info = {
        'title': '首页',
        'html': 'index.html',
    }
    return render(request, 'frame.html', locals())


@login_required
def infopage(request):
    page_info = {
        'title': '客户信息-基础信息',
        'html': 'info.html',
        'script': 'info.js',
    }
    return render(request, 'frame.html', locals())


@login_required
def attrpage(request):
    page_info = {
        'title': '客户信息-附加信息',
        'html': 'attr.html',
        'script': 'attr.js',
    }
    return render(request, 'frame.html', locals())


@login_required
def reportpage(request):
    user_cur = {}
    user_info = []
    for user in AuthUser.objects.all().order_by('-last_login'):
        tmp = {}
        for field in ('id', 'email', 'username', 'first_name', 'last_name',
                      'date_joined', 'last_login', 'is_superuser'):
            tmp[field] = getattr(user, field)
        for attr in AuthUserAttrDefine.objects.all().filter(
                userid__exact=user.id):
            tmp[attr.attr] = attr.value
        if tmp['id'] == request.user.id:
            user_cur = tmp
        user_info.append(tmp)
    # ScrapyUpdateInfo
    scrapy_info = ScrapyUpdateInfo.objects.all().order_by('-updatedt')
    static_info = {
        'data': [{
            'item': '用户数',
            'count': AuthUser.objects.all().count()
        }],
        'xkey': 'item',
        'ykey': ['count'],
        'labels': ['数量'],
    }
    for item in ScrapyUpdateInfo.objects.all().values('web', 'item').annotate(
            Count('updatedt')).values('web', 'item', 'updatedt__count'):
        # print('nxx', obj.items(), obj.keys(), obj.values())
        static_info['data'].append({
            'item': item['web'] + '_' + item['item'],
            'count': item['updatedt__count']
        })
    page_info = {
        'title': '网站信息-网站统计',
        'html': 'report.html',
        'script': 'report.js',
    }
    return render(request, 'frame.html', locals())