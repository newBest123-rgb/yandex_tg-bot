from aiogram import types

from config.api_token import PARSE_MODE_HTML

from text.text_about_the_hospital.text_about_us_contacts import TEXT_ABOUT_US_CONTACTS
from keyboards.inlain_keyboards.keyboards_back.inlain_back_questions import kb_back


async def callback_about_us_contacts(callback: types.CallbackQuery):
    if callback.data == 'about_us_contacts':
        await callback.message.reply(TEXT_ABOUT_US_CONTACTS,
                                     reply_markup=kb_back,
                                     parse_mode=PARSE_MODE_HTML)
