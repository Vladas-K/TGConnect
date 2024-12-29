from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import TelegramUser
from django.views.decorators.csrf import csrf_exempt
import uuid
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def telegram_auth(request):
    token = request.GET.get('token')
    telegram_id = request.GET.get('telegram_id')
    telegram_username = request.GET.get('telegram_username')

    logger.info(f'Получен запрос: token={token}, telegram_id={telegram_id}, telegram_username={telegram_username}')

    if token and telegram_id and telegram_username:
        user, created = User.objects.get_or_create(username=telegram_username)
        TelegramUser.objects.update_or_create(
            user=user,
            defaults={'telegram_id': telegram_id, 'telegram_username': telegram_username}
        )
        login(request, user)
        logger.info(f'Пользователь {telegram_username} авторизован успешно')
        return redirect('home')
    
    logger.warning('Ошибка авторизации: недостаточно данных')
    return redirect('home')

def home(request):
    unique_token = str(uuid.uuid4())
    logger.info(f'Создан уникальный токен: {unique_token}')
    context = {'unique_token': unique_token, 'user': request.user}
    return render(request, 'telelogin/home.html', context)
