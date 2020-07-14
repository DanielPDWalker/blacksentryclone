from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    power_crystals = models.IntegerField(default=10)
    date = models.DateTimeField(default=datetime.now, blank=False)
    hp_current = models.IntegerField(default=10)
    hp_max = models.IntegerField(default=10)
    gold = models.IntegerField(default=0)
    damage = models.IntegerField(default=10)
         
    def __str__(self):
        return self.user.username
    pass



class Enemy(models.Model):
    name = models.TextField(max_length=50, default='')
    power_crystals = models.IntegerField(default=10)
    hp_current = models.IntegerField(default=10)
    hp_max = models.IntegerField(default=10)
    gold = models.IntegerField(default=0)
    damage = models.IntegerField(default=10)

    def __str__(self):
        return self.name
    pass
