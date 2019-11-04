import random

import requests
from django.core.cache import cache

from social import cfg
from common import keys


def get_randcode(length: int) -> str:
    chars = [str(random.randint(0, 9)) for i in range(length)]
    print(chars)
    return ''.join(chars)


def send_vcode(phone):
    vcode = get_randcode(6)
    print(vcode)
    cache.set(keys.VCODE_KEY % phone, vcode, 180)  # 验证码添加到缓存,设置过期时间
    sms_args = cfg.YZX_ARGS.copy()
    sms_args['param'] = vcode
    sms_args['mobile'] = phone
    response = requests.post(cfg.YZX_API, json=sms_args)
    if response.status_code == 200:
        result = response.json()
        if result['code'] == '000000':
            return True
    return False

