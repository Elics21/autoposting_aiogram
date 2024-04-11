import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from database.models import async_main
from handlers.main_router import main_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await async_main()
    dp.include_router(main_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот Выключен")