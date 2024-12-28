from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import TelegramUser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def telegram_auth(request):
    token = request.GET.get('token')
    telegram_id = request.GET.get('telegram_id')
    telegram_username = request.GET.get('telegram_username')

    if token and telegram_id and telegram_username:
        # Находим или создаем пользователя
        user, created = User.objects.get_or_create(username=telegram_username)
        
        # Создаем или обновляем запись TelegramUser
        TelegramUser.objects.update_or_create(
            user=user,
            defaults={'telegram_id': telegram_id, 'telegram_username': telegram_username}
        )
        
        # Авторизация пользователя
        login(request, user)
        return redirect('home')
    
    return redirect('home')

def home(request):
    return render(request, 'telelogin/home.html')
