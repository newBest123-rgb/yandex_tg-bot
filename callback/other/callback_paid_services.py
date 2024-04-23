from aiogram import types

from text.text_paid_services.text_paid_services_start import PAID_SERVICES_START_TEXT
from text.text_paid_services.text_paid_services_end import PAID_SERVICES_END_TEXT

from config.api_token import PARSE_MODE_HTML

from keyboards.inlain_keyboards.keyboards_back.inlain_back_and_contacts_registr import inline_con_rigestr_kb
from keyboards.inlain_keyboards.keyboards_back.inlain_back_questions import kb_back


async def callback_query_paid_services(callback: types.CallbackQuery):
    if callback.data == 'paid_services':
        await callback.message.reply(PAID_SERVICES_START_TEXT,
                                     reply_markup=kb_back,
                                     parse_mode=PARSE_MODE_HTML)

        await callback.message.reply(PAID_SERVICES_END_TEXT,
                                     reply_markup=inline_con_rigestr_kb,
                                     parse_mode=PARSE_MODE_HTML)
