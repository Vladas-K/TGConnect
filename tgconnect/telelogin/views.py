from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

def home(request):
    return render(request, 'telelogin/home.html')

def telegram_auth(request):
    token = request.GET.get('token')
    # Логика связи токена с пользователем
    user = ...  # Получаем пользователя по токену
    login(request, user)  # Стандартный механизм авторизации Django
    return redirect('home')  # Перенаправляем на домашнюю страницу

