from aiogram import types

from config.api_token import PARSE_MODE_HTML

from text.text_frequent_questions.text_frequent_questions import FREQUENT_QUESTIONS
from keyboards.inlain_keyboards.keyboards_questions.inlain_questions import questions_kb


async def callback_query_questions(callback: types.CallbackQuery):
    if callback.data == 'chast_vopros':
        await callback.message.answer(FREQUENT_QUESTIONS,
                                      reply_markup=questions_kb,
                                      parse_mode=PARSE_MODE_HTML)
