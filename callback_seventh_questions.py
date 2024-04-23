from aiogram import types

from config.api_token import PARSE_MODE_HTML

from text.text_frequent_questions.text_seventh_questions import TEXT_SEVENTH_QUESTIONS
from keyboards.inlain_keyboards.keyboards_back.inlain_back_questions import kb_back


async def callback_query_seventh_questions(callback: types.CallbackQuery):
    if callback.data == 'seventh_questions':
        await callback.message.reply(TEXT_SEVENTH_QUESTIONS,
                                     reply_markup=kb_back,
                                     parse_mode=PARSE_MODE_HTML)
