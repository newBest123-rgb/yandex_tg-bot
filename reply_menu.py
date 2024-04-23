from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_reply_menu = ReplyKeyboardMarkup(resize_keyboard=True)

ib_reply_menu = KeyboardButton('Показать меню')

kb_reply_menu.add(ib_reply_menu)
