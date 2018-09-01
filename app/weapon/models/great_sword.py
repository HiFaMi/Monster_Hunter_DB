from django.db import models

__all__ = (
    'GreatSword',
)


class GreatSword(models.Model):

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
    # cost = models.CharField(max_length=100)

    # many to many field로 할 예정
    # first_reinforcement_material = models.CharField(max_length=200)
    # second_reinforcement_material = models.CharField(max_length=200)
    # third_reinforcement_material = models.CharField(max_length=200)
    # fourth_reinforcement_material = models.CharField(max_length=200)
    # first_fabrication_material = models.CharField(max_length=200)
    # second_fabrication_material = models.CharField(max_length=200)
    # third_fabrication_material = models.CharField(max_length=200)
    # fourth_fabrication_material = models.CharField(max_length=200)