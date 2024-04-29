from aiogram import types

from config.api_token import PARSE_MODE_HTML

from config.api_token import SIGN_UP_ADMIN

from keyboards.inlain_keyboards.keyboards_menu.inlain_menu import ikb


async def callback_admin_menu_back(callback: types.CallbackQuery):
    if callback.data == 'back_in_menu':
        await callback.message.answer(text=SIGN_UP_ADMIN,
                                      parse_mode=PARSE_MODE_HTML,
                                      reply_markup=ikb)
