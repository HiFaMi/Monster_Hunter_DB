from django.db import models

from armor.models.armor import Armor
from weapon.models import ChargeBlade, GreatSword, GunLance, Hammer, HeavyBowgun, Lance, LightBowgun, LongSword, \
    OneHandSword, SwitchAxe, TwoSwords

__all__ = (
    'Items',
)


class Items(models.Model):
    name = models.CharField(max_length=200)
    armor = models.ManyToManyField(
        Armor,
        related_name='makes_armor',
    )

    charge_blade = models.ManyToManyField(
        ChargeBlade,
        related_name='makes_charge_blade',
    )

    great_sword = models.ManyToManyField(
        GreatSword,
        related_name='makes_great_sword',
    )

    gun_lance = models.ManyToManyField(
        GunLance,
        related_name='makes_gun_lance',
    )

    hammer = models.ManyToManyField(
        Hammer,
        related_name='makes_hammer',
    )

    heavy_bowgun = models.ManyToManyField(
        HeavyBowgun,
        related_name='makes_heavy_bowgun',
    )

    lance = models.ManyToManyField(
        Lance,
        related_name='makes_lance',
    )

    light_bowgun = models.ManyToManyField(
        LightBowgun,
        related_name='makes_light_bowgun',
    )

    long_sword = models.ManyToManyField(
        LongSword,
        related_name='makes_long_sword',
    )

    one_hand_sword = models.ManyToManyField(
        OneHandSword,
        related_name='makes_one_hand_sword',
    )

    switch_axe = models.ManyToManyField(
        SwitchAxe,
        related_name='makes_switch_axe',
    )

    two_sowrds = models.ManyToManyField(
        TwoSwords,
        related_name='makes_two_swords',
    )
