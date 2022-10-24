from aiogram import types

from loader import dp

import wikipedia

wikipedia.set_lang('uz')

@dp.message_handler()
async def echo(message: types.Message):
    try:
        zzz = wikipedia.summary(message.text)
    except:
        await message.answer("Bu Haqida maqola topilmadi")
    else:
        await message.reply(zzz)

