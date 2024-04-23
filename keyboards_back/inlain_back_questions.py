from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ib_back = InlineKeyboardButton(text='⬅️Назад',
                               callback_data='back')

kb_back = InlineKeyboardMarkup()

kb_back.add(ib_back)
