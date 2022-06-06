from multiprocessing import context
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView

from .models import *
from .serializers import *


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlayerItemViewSet(viewsets.ModelViewSet):
    queryset = PlayerItem.objects.all()
    serializer_class = PlayerItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemStatViewSet(viewsets.ModelViewSet):
    queryset = ItemStat.objects.all()
    serializer_class = ItemStatSerializer


class GraphicViewSet(viewsets.ModelViewSet):
    queryset = Graphic.objects.all()
    serializer_class = GraphicSerializer


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    # Empty
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=HTTP_200_OK)


class PlayerItem(APIView):
    def get(self,request):
        item=PlayerItem.objects.all()
        serializer=PlayerItemSerializer(item,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = PlayerItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def add_player_item(request):
    item = PlayerItemSerializer(data=request.data, context={'request': request})
    if item.is_valid():
        item.save()
        return Response(item.data, status=HTTP_201_CREATED)
    return Response(item.errors, status=HTTP_400_BAD_REQUEST)