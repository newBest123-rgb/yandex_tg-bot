from aiogram import types

from data_base.db_add_users.db_add_users import id_users_admin


async def callback_admin_users_id(callback: types.CallbackQuery):
    if callback.data == 'show_users':
        await id_users_admin(callback.message)
