from django.contrib.auth.models import User
from django.db import models

from api.misc import get_upload_path


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    access_token = models.CharField(max_length=100, null=True)
    coins = models.IntegerField(default=100)

    def __str__(self):
        return f'{self.user.username} Player'

    def save(self, *args, **kwargs):
        super(Player, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category}'


class Stat(models.Model):
    name = models.CharField(max_length=80)
    value = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} | {self.item}'


class Graphic(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path)

    def __str__(self) -> str:
        return f'{self.image} | {self.item}'

