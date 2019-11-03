from django.http import JsonResponse
from django.core.cache import cache

from django.shortcuts import render
from common import keys
from common import stat
from UserApp import logics
from UserApp.models import User


def get_vcode(request):
    #获取短信验证码
    phonenum = request.Get.get('phonenum')
    # 发送验证码并检查是否发送成功
    if logics.send_vcode(phonenum):
        return JsonResponse({'code': stat.OK, 'data': None})
    else:
        return JsonResponse({'code': stat.VCODE_ERR, 'data': None})


def check_vcode(request):
    # 进行验证，并且登录或注册
    phonenum = request.Get.get('phonenum')
    vcode = request.Post.get('vcode')
    cache_vcode = cache.get(keys.VCODE_KEY % phonenum)

    if vcode and cache_vcode and vcode == cache_vcode:
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            #如果用户不存在，直接创建出来
            user = User.objects.create(
                phonenum=phonenum,
                nickname=phonenum,
            )
        request.session['uid'] = user.id
        return JsonResponse({'code': stat.OK, 'data': user.to_dict()})

    else:
        return JsonResponse({'code': stat.INVILD_VCODE, 'data': None})


