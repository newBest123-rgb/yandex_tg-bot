from aiogram import types

from config.api_token import PARSE_MODE_HTML

from text.text_regestratura.text_regestratura import REGESTRATURE_TEXT
from keyboards.inlain_keyboards.keyboards_back.inlain_back_questions import kb_back


async def callback_query_contacts_rigestr(callback: types.CallbackQuery):
    if callback.data == 'contacts_rigestr':
        await callback.message.reply(REGESTRATURE_TEXT,
                                     reply_markup=kb_back,
                                     parse_mode=PARSE_MODE_HTML)

        await callback.message.delete()
