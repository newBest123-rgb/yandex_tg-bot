from aiogram import types

from text.text_application.text_application import APLICATION_TEXT
from data_base.db_application.db_application import recording_users


async def callback_query_aplication(callback: types.CallbackQuery):
    if callback.data == 'application':
        await recording_users(callback.message)
        await callback.answer(APLICATION_TEXT)
