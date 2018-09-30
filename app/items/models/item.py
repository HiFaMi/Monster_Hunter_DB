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
        null=True,
    )

    charge_blade = models.ManyToManyField(
        ChargeBlade,
        related_name='makes_charge_blade',
        null=True,
    )

    great_sword = models.ManyToManyField(
        GreatSword,
        related_name='makes_great_sword',
        null=True,
    )

    gun_lance = models.ManyToManyField(
        GunLance,
        related_name='makes_gun_lance',
        null=True,
    )

    hammer = models.ManyToManyField(
        Hammer,
        related_name='makes_hammer',
        null=True,
    )

    heavy_bowgun = models.ManyToManyField(
        HeavyBowgun,
        related_name='makes_heavy_bowgun',
        null=True,
    )

    lance = models.ManyToManyField(
        Lance,
        related_name='makes_lance',
        null=True,
    )

    light_bowgun = models.ManyToManyField(
        LightBowgun,
        related_name='makes_light_bowgun',
        null=True,
    )

    long_sword = models.ManyToManyField(
        LongSword,
        related_name='makes_long_sword',
        null=True,
    )

    one_hand_sword = models.ManyToManyField(
        OneHandSword,
        related_name='makes_one_hand_sword',
        null=True,
    )

    switch_axe = models.ManyToManyField(
        SwitchAxe,
        related_name='makes_switch_axe',
        null=True,
    )

    two_sowrds = models.ManyToManyField(
        TwoSwords,
        related_name='makes_two_swords',
        null=True,
    )
