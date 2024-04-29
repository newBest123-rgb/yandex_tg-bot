from aiogram import types
import sqlite3

from keyboards.inlain_keyboards.inlain_keyboards_admin.inlain_keyboards_admin_panel_users import ikb_admin_show_users


async def show_users(message: types.Message):
    sqlite_connection = sqlite3.connect('users.db')
    cursor = sqlite_connection.cursor()

    cursor.execute("""SELECT * from users_id""")
    records = cursor.fetchall()

    len_records = len(records)

    user_567890 = 'пользователей'

    user_1 = 'пользователь'

    user_234 = 'пользователя'

    if len_records % 10 == 1:
        await message.bot.send_message(chat_id=message.from_user.id,
                                       text=f'Всего {str(len_records)} {user_1}',
                                       reply_markup=ikb_admin_show_users)

    elif 5 <= len_records % 10 <= 9 or len_records % 10 == 0:
        await message.bot.send_message(chat_id=message.from_user.id,
                                       text=f'Всего {str(len_records)} {user_567890}',
                                       reply_markup=ikb_admin_show_users)

    elif 2 <= len_records % 10 <= 4:
        await message.bot.send_message(chat_id=message.from_user.id,
                                       text=f'Всего {str(len_records)} {user_234}',
                                       reply_markup=ikb_admin_show_users)
