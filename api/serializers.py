from dataclasses import field
from http import server
from wsgiref.simple_server import server_version
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class PlayerSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    email = serializers.SerializerMethodField('get_email')

    class Meta:
        model = Player
        fields = ['url', 'username', 'email', 'coins']

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email


class PlayerItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerItem
        fields = ['name', 'price', 'category', 'player']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name'] 


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price', 'category']


class ItemStatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemStat
        fields = ['name', 'value', 'item']


class GraphicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Graphic
        fields = ['image', 'item']