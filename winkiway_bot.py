import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# Токен бота
BOT_TOKEN = os.getenv('BOT_TOKEN', '8388195492:AAHnAu-qyd_Jn9H9o2BKMmVxVEgD2PSTKe8')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def create_links_keyboard():
    """Клавиатура с ссылками"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📺 Rutube", url="https://rutube.ru/channel/45561662")],
            [InlineKeyboardButton(text="🎮 Twitch", url="https://www.twitch.tv/phoenix_so3?sr=a")],
            [InlineKeyboardButton(text="🎮 Commander Pass", url="https://link.standoff2.com/ru/referral/bind/199997168")],
            [InlineKeyboardButton(text="📢 Telegram канал", url="https://t.me/GoldnPhonX")]
        ]
    )
    return keyboard

@dp.message(Command("start"))
async def start_command(message: types.Message):
    """Обработчик команды /start"""
    await message.answer(
        "Привет. Это бот канала https://t.me/GoldnPhonX\n\n"
        "Вот все ссылки:",
        reply_markup=create_links_keyboard()
    )

@dp.message(Command("status"))
async def status_command(message: types.Message):
    """Обработчик команды /status"""
    await message.answer("🟢 Бот работает на Railway!")

@dp.message()
async def echo_message(message: types.Message):
    """Эхо-ответ"""
    await message.answer(f"🔁 Echo: {message.text}")

async def main():
    """Основная функция"""
    print("🚀 Winkiway Bot запущен!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
