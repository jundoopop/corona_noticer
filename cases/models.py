from django.db import models


# Create your models here.

class DailyCorona(models.Model):
    date = models.DateField(primary_key=True)
    positive = models.IntegerField(default=0)
    domestic = models.IntegerField(default=0)
    oversea = models.IntegerField(default=0)
    cured = models.IntegerField(default=0)
    quarantined = models.IntegerField(default=0)
    death = models.IntegerField(default=0)
    # tests = models.IntegerField(default=0)


class SumCorona(models.Model):
    date = models.DateField(primary_key=True)
    positive = models.IntegerField(default=0)
    # domestic = models.IntegerField(default=0)
    # oversea = models.IntegerField(default=0)
    death = models.IntegerField(default=0)
    cured = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)
    test = models.IntegerField(default=0)
    in_test = models.IntegerField(default=0)
    quarantined = models.IntegerField(default=0)
    pos_neg = models.IntegerField(default=0)