from aiogram import types

from config.api_token import PARSE_MODE_HTML

from text.text_frequent_questions.text_fiveth_questions import TEXT_FIVETH_QUESTIONS
from keyboards.inlain_keyboards.keyboards_back.inlain_back_questions import kb_back


async def callback_query_fiveth_questions(callback: types.CallbackQuery):
    if callback.data == 'fiveth_questions':
        await callback.message.reply(TEXT_FIVETH_QUESTIONS,
                                     reply_markup=kb_back,
                                     parse_mode=PARSE_MODE_HTML)
