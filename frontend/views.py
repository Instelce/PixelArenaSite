from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.views import LoginView

from .forms import *


def home(request):
    return render(request, 'frontend/home.html')

def download(request):
    return render(request, 'frontend/download.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} account has been created !')
            return redirect('download')
    else:
        form = UserRegisterForm()

    return render(request, 'frontend/register.html', {'form': form, 'title': 'Sign Up'})


class Login(LoginView):
    def get_success_url(self):
        user = self.request.user
        return reverse('home')