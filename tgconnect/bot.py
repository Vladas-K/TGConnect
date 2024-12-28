import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import aiohttp

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    token = context.args[0] if context.args else None
    if token:
        telegram_id = update.effective_user.id
        telegram_username = update.effective_user.username

        async with aiohttp.ClientSession() as session:
            async with session.get('http://127.0.0.1:8000/telegram-auth/', params={
                'token': token,
                'telegram_id': telegram_id,
                'telegram_username': telegram_username
            }) as response:
                if response.status == 200:
                    await update.message.reply_text('Авторизация выполнена успешно! Возвращайтесь на сайт.')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levellevelname)s - %(message)s',
    level=logging.INFO
)

def main():
    application = ApplicationBuilder().token("7614123688:AAEw_pIyN3r_1WgLs9QiAXMsMXvCroH8rHQ").build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    application.run_polling()

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    main()