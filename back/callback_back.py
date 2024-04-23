from aiogram import types


async def callback_back_query_questions(callback: types.CallbackQuery):
    if callback.data == 'back':
        await callback.message.delete()
