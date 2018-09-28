from django.db import models

from armor.models.armor import Armor
from items.models.accessory import Accessory

__all__ = (
    'Skill',
)


class Skill(models.Model):
    name = models.CharField(max_length=150)
    detail = models.CharField(max_length=300)
    accessory = models.ManyToManyField(
        Accessory,
        related_name='accessory_skills',
    )
    armor = models.ManyToManyField(
        Armor,
        related_name='armor_skill',
    )
