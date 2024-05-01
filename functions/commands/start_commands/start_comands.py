from aiogram import types

from config.api_token import PARSE_MODE_HTML
from config.api_token import SIGN_UP_ADMIN
from config.api_token import ADMIN_ID

from text.text_commands_bot.text_command_start import START_TEXT

from keyboards.inlain_keyboards.keyboards_menu.inlain_menu import ikb
from keyboards.inlain_keyboards.inlain_keyboards_admin.inlain_keyboards_admin_menu import ikb_admin
from data_base.db_users.db_users import recording_users


async def func_start_start_bot(message: types.Message):
    if message.from_user.id == int(ADMIN_ID):
        await message.answer(text=SIGN_UP_ADMIN,
                             reply_markup=ikb_admin)
    else:
        await message.bot.send_message(chat_id=message.from_user.id,
                                       text=START_TEXT,
                                       reply_markup=ikb,
                                       parse_mode=PARSE_MODE_HTML)

    await recording_users(message)
