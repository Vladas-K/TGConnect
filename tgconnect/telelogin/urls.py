from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('telegram-auth/', views.telegram_auth, name='telegram_auth'),
]
