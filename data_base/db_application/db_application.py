from aiogram import types
import sqlite3


async def recording_users(message: types.Message):
    connect = sqlite3.connect('application.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS application_users_id(id INTEGER)""")

    connect.commit()

    table_people_id = message.chat.id

    cursor.execute(f"SELECT id FROM application_users_id WHERE id = {table_people_id}")
    user_data = cursor.fetchone()

    if user_data is None:
        users_id = [message.chat.id]
        cursor.execute("INSERT INTO application_users_id VALUES(?);", users_id)
        connect.commit()

    cursor.close()
