from django.db import models

__all__ = (
    'Items',
)


class Items(models.Model):
    name = models.CharField(max_length=200)
