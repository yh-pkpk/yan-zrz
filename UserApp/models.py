
from django.db import models


class UserappUser(models.Model):
    phonenum = models.CharField(unique=True, max_length=15)
    nickname = models.CharField(max_length=20)
    sex = models.CharField(max_length=8)
    birthday = models.DateField()
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'UserApp'

