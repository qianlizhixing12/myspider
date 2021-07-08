from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.apps import apps
from django.core import serializers
from gaokao.models import GaokaoSchool
from custom.models import AuthUserAttrDefine
from .tool import user_to_response
import json


def data_from_form(request):
    data = {}
    for field in request.POST:
        if request.POST.get(field):
            data[field] = request.POST.get(field)
    return data


def data_from_json(request):
    data = {}
    body = json.loads(request.body)
    for field in body:
        data[field] = body[field]
    return data


def user_from_request(request):
    if request.method == 'GET':
        return get_user(request)
    elif request.method == 'POST':
        if request.META['CONTENT_TYPE'] in ('application/json',
                                            'application/json;charset=UTF-8'):
            return data_from_json(request)
        elif request.META[
                'CONTENT_TYPE'] == 'application/x-www-form-urlencoded':
            return data_from_form(request)
    return None


def user_check_simple(user):
    result = {'succ': True, 'msg': []}
    # 校验用户
    if not user.get('username'):
        result['succ'] = False
        result['msg'].append('用户名不能为空')
    elif len(user['username']) < 3:
        result['succ'] = False
        result['msg'].append('用户名不能少于3个字符')
    # 校验密码
    if not user.get('password'):
        result['succ'] = False
        result['msg'].append('密码不能为空')
    elif len(user['password']) < 10:
        result['succ'] = False
        result['msg'].append('密码不能少于10个字符')
    return result


def user_check_full(user):
    result = user_check_simple(user)
    if not user.get('email'):
        result['succ'] = False
        result['msg'].append('邮箱不能为空')
    # elif len(user['username']) < 3:
    #     result['succ'] = False
    #     result['msg'].append('用户名不能少于3个字符')
    return result


def result_to_response(result):
    result['msg'] = '\n'.join(result['msg'])
    return JsonResponse(result, charset='utf-8', status=200)


@csrf_exempt
def custom_logindo(request):
    userinfo = user_from_request(request)
    result = user_check_simple(userinfo)
    if result['succ']:
        usersucc = authenticate(username=userinfo['username'],
                                password=userinfo['password'])
        if usersucc:
            login(request, usersucc)
            result['msg'].append('登录成功!')
        else:
            result['succ'] = False
            result['msg'].append('用户或密码错误!')
            # return HttpResponseRedirect("/index.html")
            # return HttpResponse(json.dumps(data),
            #                     content_type='application/json',
            #                     charset='utf-8',
            #                     status=401)
            # return JsonResponse(data, charset='utf-8', status=401)
    return result_to_response(result)


@csrf_exempt
def custom_createdo(request):
    userinfo = user_from_request(request)
    result = user_check_full(userinfo)
    if result['succ']:
        user = User.objects.create_user(
            username=userinfo['username'],
            email=userinfo['email'],
            password=userinfo['password'],
        )
        if user:
            result['msg'].append('创建成功!')
        else:
            result['succ'] = False
            result['msg'].append('创建失败!')
    return result_to_response(result)


@login_required
@csrf_exempt
def custom_logoutdo(request):
    if request.method == 'GET':
        logout(request)
        result = {'succ': True, 'msg': ['退出成功!']}
        return result_to_response(result)


@login_required
@csrf_exempt
def custom_getdo(request):
    user_model = user_from_request(request)
    user = user_to_response(user_model)
    result = {'succ': True, 'msg': ['获取用户认证信息成功!'], 'user': user}
    return result_to_response(result)


@login_required
@csrf_exempt
def custom_editdo(request):
    if request.method == 'POST':
        n_user = user_from_request(request)
        result = user_check_full(n_user)
        if result['succ']:
            user = request.user
            # user = User.objects.get(id=request.user.id)
            edit = False
            for field in n_user:
                if field != 'password':
                    if n_user[field] != getattr(user, field):
                        setattr(user, field, n_user[field])
                        edit = True
                elif field == 'password':
                    if n_user['password'] != '0000000000':
                        user.set_password(n_user['password'])
                        edit = True
            if edit:
                user.save()
                result['msg'].append('修改认证信息成功!')
            else:
                result['msg'].append('无需修改!')
        return result_to_response(result)


@login_required
@csrf_exempt
def custom_attr_getdo(request):
    user = get_user(request)
    attrs = AuthUserAttrDefine.objects.all().filter(userid__exact=user.id)
    # result = {
    #     'succ': True,
    #     'msg': ['获取附加信息成功!'],
    #     'attr': serializers.serialize('json', attr)
    # }
    result = {'succ': True, 'msg': ['获取附加信息成功!'], 'attrs': {}}
    for attr in attrs:
        result['attrs'][attr.attr] = attr.value
    return result_to_response(result)


@login_required
@csrf_exempt
def custom_attr_editdo(request):
    if request.method == 'POST':
        user = get_user(request)
        params = data_from_form(request)
        for key in params:
            # obj = AuthUserAttrDefine.objects.all().filter(
            #     userid__exact=user.id).filter(attr__exact=key)
            try:
                obj = AuthUserAttrDefine.objects.all().get(userid=user.id,
                                                           attr=key)
                obj.value = params[key]
                obj.save()
            except Exception as e:
                obj = AuthUserAttrDefine.objects.create(userid=user.id,
                                                        attr=key,
                                                        value=params[key])
                obj.save()
        result = {'succ': True, 'msg': ['修改附加信息成功！']}
        return result_to_response(result)


@login_required
@csrf_exempt
def gaokao_scoollist_getdo(request):
    if request.method == 'POST':
        param = json.loads(request.body)
        updatedt = param['updatedt']
        schoolkey = param['schoolkey']
        length = param['length']
        start = param['start']
        #采集时间
        datas = GaokaoSchool.objects.all().filter(updatedt__exact=updatedt)
        # .order_by("-star")
        #名称过滤
        if schoolkey:
            datas = datas.filter(name__icontains=schoolkey)
        result = {
            'recordsTotal': datas.count(),
            'length': length,
            'strat': start + length
        }
        result['data'] = list(map(model_to_dict, datas[start:start + length]))
        return JsonResponse(result, charset='utf-8')
