from rest_framework import viewsets, permissions
from .models import Player, Category, Item, Graphic
from .serializers import CategorySerializer, GraphicSerializer, ItemSerializer, PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class GraphicViewSet(viewsets.ModelViewSet):
    queryset = Graphic.objects.all()
    serializer_class = GraphicSerializer