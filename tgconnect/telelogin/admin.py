from django.contrib import admin
from .models import TelegramUser

@admin.register(TelegramUser)
class TelegramUser(admin.ModelAdmin):
        list_display = ('user', 'telegram_id', 'telegram_username')

