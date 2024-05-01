from aiogram import types

from text.text_commands_bot.text_command_contacts import TEXT_COMMAND_CONTACTS
from keyboards.inlain_keyboards.keyboards_back.inlain_back_questions import kb_back
from config.api_token import PARSE_MODE_HTML


async def func_contacts_bot(message: types.Message):
    await message.bot.send_message(chat_id=message.from_user.id,
                                   text=TEXT_COMMAND_CONTACTS,
                                   reply_markup=kb_back,
                                   parse_mode=PARSE_MODE_HTML)

    await message.delete()
