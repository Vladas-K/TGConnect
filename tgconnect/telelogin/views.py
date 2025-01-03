from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import TelegramUser
from django.views.decorators.csrf import csrf_exempt
import uuid
import logging

logger = logging.getLogger('telelogin')


@csrf_exempt
def telegram_auth(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        telegram_id = request.POST.get('telegram_id')
        telegram_username = request.POST.get('telegram_username')

        if token and telegram_id and telegram_username:
            user, created = User.objects.get_or_create(username=telegram_username)
            TelegramUser.objects.update_or_create(
                user=user,
                defaults={'telegram_id': telegram_id, 'telegram_username': telegram_username}
            )
            login(request, user)
            return redirect('home')
    
    logger.warning('Ошибка авторизации: недостаточно данных')
    return redirect('home')


def home(request):
    unique_token = str(uuid.uuid4())
    bot_name = settings.BOT_NAME
    context = {'unique_token': unique_token, 'user': request.user, 'bot_name': bot_name}
    return render(request, 'telelogin/home.html', context)
