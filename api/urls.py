from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views


router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'graphics', views.GraphicViewSet)
router.register(r'stats', views.StatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.login),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
