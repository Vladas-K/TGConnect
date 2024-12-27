from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('telelegram-auth/', views.telegram_auth, name='telegram_auth'),  # Маршрут для обратного вызова
]
