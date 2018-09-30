from django.db import models

__all__ = (
    'Armor',
)


class Armor(models.Model):
    name = models.CharField(max_length=100)
    equip_region = models.CharField(max_length=100)
    rare = models.CharField(max_length=50)
    cost = models.IntegerField()
    defense = models.IntegerField()
    vs_fire = models.IntegerField()
    vs_water = models.IntegerField()
    vs_thunder = models.IntegerField()
    vs_ice = models.IntegerField()
    vs_dragon = models.IntegerField()
    slot = models.CharField(max_length=50)

