import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    print("❌ Ошибка: BOT_TOKEN не установлен!")
    exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def create_links_keyboard():
    """Создает клавиатуру с ссылками"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📺 Rutube", url="https://rutube.ru/channel/45561662")],
            [InlineKeyboardButton(text="🎮 Twitch", url="https://www.twitch.tv/phoenix_so3?sr=a")],
            [InlineKeyboardButton(text="🎮 Commander Pass", url="https://link.standoff2.com/ru/referral/bind/199997168")],
            [InlineKeyboardButton(text="📢 Telegram канал", url="https://t.me/GoldnPhonX")]
        ]
    )

@dp.message(Command("start"))
async def start_command(message: types.Message):
    """Обработчик команды /start"""
    await message.answer(
        "Привет! Это бот канала https://t.me/GoldnPhonX\n\n"
        "👇 Вот все ссылки:",
        reply_markup=create_links_keyboard()
    )

@dp.message(Command("status"))
async def status_command(message: types.Message):
    """Обработчик команды /status"""
    await message.answer("🟢 Бот работает на Render.com!")

@dp.message()
async def echo_message(message: types.Message):
    """Эхо-ответ на любое сообщение"""
    await message.answer(f"🔁 Echo: {message.text}")

async def main():
    """Основная функция"""
    print("🚀 Winkiway Bot запущен на Render!")
    print("🤖 Ожидание сообщений...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
