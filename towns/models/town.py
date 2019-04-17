from django.db import models


class Town(models.Model):
    name = models.CharField(max_length=100)
    town_code = models.IntegerField()
    department_code = models.IntegerField()
    population = models.IntegerField()

