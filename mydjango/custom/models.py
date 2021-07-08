from django.db import models


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserAttrDefine(models.Model):
    userid = models.IntegerField()
    attr = models.CharField(max_length=50)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'auth_user_attr_define'
        unique_together = (('userid', 'attr'),)


class ScrapyUpdateInfo(models.Model):
    id = models.AutoField(primary_key=True)
    web = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    updatedt = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'scrapy_update_info'