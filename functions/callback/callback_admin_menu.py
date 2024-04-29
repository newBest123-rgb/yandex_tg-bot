from aiogram import types

from config.api_token import PARSE_MODE_HTML

from text.text_admin.text_admin_action import TEXT_ADMIN_ACTIONS

from keyboards.reply_keyboards.keyboards_admin.reply_admin_panel import kb_reply_admin_panel


async def callback_admin_menu(callback: types.CallbackQuery):
    if callback.data == 'admin_panel':
        await callback.message.answer(text=TEXT_ADMIN_ACTIONS,
                                      parse_mode=PARSE_MODE_HTML,
                                      reply_markup=kb_reply_admin_panel)
