from dataclasses import field
from rest_framework import serializers
from .models import Graphic, Player, Category, Item
from django.contrib.auth.models import User


class PlayerSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    email = serializers.SerializerMethodField('get_email')
    password = serializers.SerializerMethodField('get_password')

    class Meta:
        model = Player
        fields = ['url', 'username', 'email', 'password', 'access_token', 'coins']

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    def get_password(self, obj):
        return obj.user.password


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name'] 


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price', 'category']


class GraphicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Graphic
        fields = ['image', 'item']