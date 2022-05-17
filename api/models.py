from django.contrib.auth.models import User
from django.db import models


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=60)

    coins = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} Player'

    def save(self, *args, **kwargs):
        super(Player, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=60)


class Item(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    graphics = models.ImageField(upload_to='graphics_item')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


