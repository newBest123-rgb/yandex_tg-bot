from aiogram import types

from text.text_application.text_application import APLICATION_TEXT


async def callback_query_aplication(callback: types.CallbackQuery):
    if callback.data == 'application':
        await callback.answer(APLICATION_TEXT)
