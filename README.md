# TGConnect

Этот проект позволяет пользователям аутентифицироваться в веб-приложении Django через Telegram.

## Установка

1. Клонируйте репозиторий и перейдите в его директорию:

   ```bash
   git clone git@github.com:Vladas-K/TGConnect.git
   cd TGConnect
   ```

2. Создайте виртуальное окружение и установите зависимости:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Настройте файл `.env`:

   ```plaintext
   TOKEN=<your-telegram-bot-token>
   BOT_NAME=<your-bot-name>
   ```

4. Примените миграции базы данных:

   ```bash
   python manage.py migrate
   ```

5. Запустите сервер Django и Telegram бота:

   ```bash
   python manage.py runserver
   python bot.py
   ```

## Использование

1. Перейдите на главную страницу веб-приложения, где будет отображаться кнопка "Войти через Telegram".
2. Нажмите на кнопку, чтобы быть перенаправленным в Telegram-бота. Ссылка содержит команду `/start` с уникальным токеном.
3. В Telegram отправьте команду `/start`, чтобы передать токен боту.
4. Бот передаст токен серверу Django, который свяжет ваш Telegram-аккаунт с вашим профилем на веб-сайте.
5. Веб-страница автоматически обновится, отобразив ваше имя или никнейм из Telegram. Вы будете авторизованы через стандартные механизмы Django.

## Основные зависимости

- `Django`
- `python-telegram-bot`
- `python-dotenv`
- `aiohttp`

## Автор

Владас Куодис