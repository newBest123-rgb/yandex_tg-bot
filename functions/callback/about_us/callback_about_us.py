from aiogram import types

from config.api_token import PARSE_MODE_HTML

from text.text_about_the_hospital.text_about_us import TEXT_CONTACTS_HOSPITAL
from keyboards.inlain_keyboards.keyboards_about_us.inlain_about_us import about_us_kb


async def callback_contacts_hospital(callback: types.CallbackQuery):
    if callback.data == 'about_us':
        await callback.message.answer(TEXT_CONTACTS_HOSPITAL,
                                      reply_markup=about_us_kb,
                                      parse_mode=PARSE_MODE_HTML)
