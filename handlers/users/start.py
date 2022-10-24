from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = f"Bu botimiz <b>WikiPedia</b>dan ma'lumot\nolish uchun xizmat qiladi!!!\nSo'z yuborib ko'ring"
    await message.reply(f"Assalomu alaykum, {message.from_user.full_name}!")
    await message.answer(text)

