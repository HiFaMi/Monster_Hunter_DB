from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=150)
    detail = models.CharField(max_length=300)

