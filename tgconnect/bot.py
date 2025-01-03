import os
import logging
import asyncio
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import aiohttp


load_dotenv()

bot_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info('Команда /start получена')
    token = context.args[0] if context.args else None
    if token:
        logger.info(f'Получен токен: {token}')
        telegram_id = update.effective_user.id
        telegram_username = update.effective_user.username
        logger.info(f'Telegram ID: {telegram_id}, Telegram Username: {telegram_username}')

        async with aiohttp.ClientSession() as session:
            async with session.post('http://127.0.0.1:8000/telegram-auth/', data={
                'token': token,
                'telegram_id': telegram_id,
                'telegram_username': telegram_username
            }) as response:
                if response.status == 200:
                    await update.message.reply_text('Авторизация выполнена успешно! Возвращайтесь на сайт')
                else:
                    await update.message.reply_text('Произошла ошибка при авторизации. Попробуйте еще раз.')
    else:
        await update.message.reply_text('Не удалось получить токен. Пожалуйста, повторите попытку.')


def main():
    application = ApplicationBuilder().token(bot_token).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    logger.info("Бот запущен и ожидает команды.")
    application.run_polling()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    main()
