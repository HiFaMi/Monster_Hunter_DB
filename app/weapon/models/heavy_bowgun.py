from django.db import models

__all__ = (
    'HeavyBowgun',
)


class HeavyBowgun(models.Model):
    name = models.CharField(max_length=200)
    rare = models.IntegerField()
    produce = models.CharField(max_length=100)
    attack = models.IntegerField()
    recoil = models.CharField(max_length=50)
    fatal_blow = models.IntegerField()
    slot = models.CharField(max_length=100)
    custom_mod = models.CharField(max_length=50)
    special_ammo = models.CharField(max_length=200)
