from aiogram import types

from config.api_token import PARSE_MODE_HTML
from keyboards.reply_keyboards.keyboards_menu.reply_menu import kb_reply_menu
from functions.commands.other_commands.help_command import HELP_COMMAND


async def func_help_bot(message: types.Message):
    await message.bot.send_message(chat_id=message.from_user.id,
                                   text=HELP_COMMAND,
                                   reply_markup=kb_reply_menu,
                                   parse_mode=PARSE_MODE_HTML)
    await message.delete()
