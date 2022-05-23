from django.shortcuts import render


def home(request):
    return render(request, 'frontend/home.html')

def login(request):
    return render(request, 'frontend/login.html', {'title': 'Login'})

def register(request):
    return render(request, 'frontend/register.html', {'title': 'Sign Up'})