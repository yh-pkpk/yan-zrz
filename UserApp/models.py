
from django.db import models


class User(models.Model):
    phonenum = models.CharField(unique=True, max_length=15)
    nickname = models.CharField(max_length=20)
    sex = models.CharField(max_length=8)
    birthday = models.DateField(default='1990-1-1')
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'User'

    def to_dict(self):
        return {
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'sex': self.sex,
            'birthday': str(self.birthday),
            'avatar': self.avatar,
            'location': self.location,
        }
