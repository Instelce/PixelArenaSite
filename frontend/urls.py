from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('download', views.download, name='download'),
    path('login', views.Login.as_view(template_name='frontend/login.html', extra_context={'title': 'Login'}), name='login'),
    path('register', views.register, name='register')
]
