from aiogram import types

from text.text_commands_bot.text_command_start import START_TEXT
from keyboards.inlain_keyboards.keyboards_menu.inlain_menu import ikb
from config.api_token import PARSE_MODE_HTML


async def func_pokaz_menu_bot(message: types.Message):
    await message.bot.send_message(chat_id=message.from_user.id,
                                   text=START_TEXT,
                                   reply_markup=ikb,
                                   parse_mode=PARSE_MODE_HTML)

    await message.delete()
