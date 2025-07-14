import os
import django
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

# .env fayldan o'qish
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Django sozlash
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edu_project.settings")  # loyihangiz nomiga mos yozing
django.setup()

# Botni va dispatcher'ni yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Router import
from handlers import router

# Routerni dispatcherga ulash
dp.include_router(router)


async def main():
    print("✅ Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
