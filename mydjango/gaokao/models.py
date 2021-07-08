from django.db import models


class GaokaoSchool(models.Model):
    id = models.AutoField(primary_key=True)
    updatedt = models.CharField(max_length=25)
    name = models.TextField()
    city = models.TextField()
    dep = models.TextField()
    style = models.TextField()
    level = models.TextField()
    star = models.TextField()

    class Meta:
        managed = False
        db_table = 'gaokao_school'