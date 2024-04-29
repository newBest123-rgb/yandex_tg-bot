from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_reply_admin_panel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

ib_reply_admin_panel_reviews = KeyboardButton('Пользователи')

ib_reply_admin_panel_complaints = KeyboardButton('Кто подал заявку')


kb_reply_admin_panel.add(ib_reply_admin_panel_reviews)
kb_reply_admin_panel.add(ib_reply_admin_panel_complaints)
