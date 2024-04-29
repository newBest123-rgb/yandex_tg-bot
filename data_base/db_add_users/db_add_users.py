from aiogram import types
import sqlite3


async def id_users_admin(message: types.Message):
    sqlite_connection = sqlite3.connect('application.db')
    cursor = sqlite_connection.cursor()

    cursor.execute("""SELECT * from application_users_id""")
    records = cursor.fetchall()

    count = 1

    await message.answer('ID пользователей, которые подали заявку👇',)

    for row in records:
        await message.answer(f'{count}) {row[0]}')
        count += 1
