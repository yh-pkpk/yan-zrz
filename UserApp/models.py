
from django.db import models


class User(models.Model):
    SEX = (
        ('male', '男性'),
        ('female', '女性'),
    )
    LOCATION = (
        ('北京','北京'),
        ('上海','上海'),
        ('广东','广东'),
        ('广东','广东'),
        ('重庆','重庆'),
        ('西安','西安'),
        ('武汉','武汉'),
        ('长沙','长沙'),
    )
    phonenum = models.CharField(unique=True, max_length=20, verbose_name='手机号')
    nickname = models.CharField(max_length=32, verbose_name='昵称')
    sex = models.CharField(max_length=8, choices=SEX, verbose_name='性别', default='male')
    birthday = models.DateField(default='1990-1-1', verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=20, choices=LOCATION, default='北京', verbose_name='常居地')

    class Meta:
        db_table = 'user'

    def to_dict(self):
        return {
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'sex': self.sex,
            'birthday': str(self.birthday),
            'avatar': self.avatar,
            'location': self.location,
        }
