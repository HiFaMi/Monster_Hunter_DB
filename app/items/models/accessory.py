from django.db import models

__all__ = (
    'Accessory',
)


class Accessory(models.Model):
    name = models.CharField(max_length=200)
    slot_lv = models.CharField(max_length=50)
    rare = models.CharField(max_length=50)
