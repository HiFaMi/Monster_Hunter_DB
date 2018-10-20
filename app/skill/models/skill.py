from django.db import models

from armor.models.armor import Armor
from items.models.accessory import Accessory

__all__ = (
    'Skill',
)


class Skill(models.Model):
    name = models.CharField(max_length=150)
    Lv1 = models.CharField(max_length=300, null=True)
    Lv2 = models.CharField(max_length=300, null=True)
    Lv3 = models.CharField(max_length=300, null=True)
    Lv4 = models.CharField(max_length=300, null=True)
    Lv5 = models.CharField(max_length=300, null=True)

    accessory = models.ManyToManyField(
        Accessory,
        related_name='accessory_skills',
    )
    armor = models.ManyToManyField(
        Armor,
        related_name='armor_skill',
    )
