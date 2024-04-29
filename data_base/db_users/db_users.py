from aiogram import types
import sqlite3


async def recording_users(message: types.Message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users_id(id INTEGER)""")

    connect.commit()

    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM users_id WHERE id = {people_id}")
    data = cursor.fetchone()

    if data is None:
        users_id = [message.chat.id]
        cursor.execute("INSERT INTO users_id VALUES(?);", users_id)
        connect.commit()
