from django.db import models

__all__ = (
    'GunLance',
)


class GunLance(models.Model):
    name = models.CharField(max_length=200)
    rare = models.IntegerField()
    produce = models.CharField(max_length=100)
    attack = models.IntegerField()
    defense = models.IntegerField()
    weapon_property = models.CharField(max_length=100)
    weapon_property_fiqure = models.CharField(max_length=100)
    abnormal_condition = models.CharField(max_length=100)
    abnormal_condition_figure = models.CharField(max_length=100)
    fatal_blow = models.IntegerField()
    slot = models.CharField(max_length=100)
    cannon = models.CharField(max_length=100)
