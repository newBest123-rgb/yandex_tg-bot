from aiogram import types

from config.api_token import PARSE_MODE_HTML

from text.text_about_the_hospital.text_about_us_guide import TEXT_ABOUT_US_GUIDE
from keyboards.inlain_keyboards.keyboards_back.inlain_back_and_guide import kb_back_and_guide


async def callback_about_us_guide(callback: types.CallbackQuery):
    if callback.data == 'about_us_guide':
        await callback.message.reply(TEXT_ABOUT_US_GUIDE,
                                     reply_markup=kb_back_and_guide,
                                     parse_mode=PARSE_MODE_HTML)
